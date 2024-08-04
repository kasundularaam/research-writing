import os
import json
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Dict, Union
from llm_lib import llm

# Ensure you have set your OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = "your-api-key"


class BestModel(BaseModel):
    name: str = Field(
        description="Name of the best performing model or technique")
    performance: Dict[str, Union[float, str]] = Field(
        description="Performance scores for the best model")


class PerformanceEvaluation(BaseModel):
    metrics: List[str] = Field(
        description="Performance metrics used to evaluate the bug prediction model(s)")
    baseline_models: List[str] = Field(
        description="Baseline models or techniques used for comparison")
    best_model: BestModel = Field(
        description="Best performing model and its performance scores")


class SourceLocations(BaseModel):
    performance_evaluation: str = Field(
        description="Location of performance evaluation information")


class ExtractedInfo(BaseModel):
    performance_evaluation: PerformanceEvaluation
    source_locations: SourceLocations


parser = PydanticOutputParser(pydantic_object=ExtractedInfo)

prompt_template = """
For the research paper, please extract the following information about performance evaluation and provide it in a JSON format:
4. Performance Evaluation:
   - List all performance metrics used to evaluate the bug prediction model(s)
   - Baseline models or techniques used for comparison
   - Best performing model/technique and its performance scores
For each piece of information, please include the section or page number where it was found in the paper.

{format_instructions}

Please follow these guidelines:
1. In the "metrics" array, list all performance metrics mentioned (e.g., accuracy, precision, recall, F1-score, AUC-ROC).
2. In the "baseline_models" array, list all models or techniques used as baselines or for comparison.
3. For the "best_model":
   - "name": Provide the name of the best performing model or technique.
   - "performance": Include a key-value pair for each performance metric reported for this model. Use numeric values for the scores.
4. If any information is not available or unclear in the paper, please use "N/A" for string values, an empty array [] for list values, and null for numeric values.
5. In "source_locations", provide the section or page numbers where the performance evaluation information was found.
Ensure that all relevant performance evaluation information is captured, including any statistical tests or cross-validation procedures mentioned.

Here is the content of the research paper:
{paper_content}

Provide the extracted information in the specified JSON format.
"""

prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | llm


def process_pdf(file_path, output_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    content = " ".join([page.page_content for page in pages])

    result = chain.invoke({
        "format_instructions": parser.get_format_instructions(),
        "paper_content": content
    })

    # Try to extract JSON from the result
    json_match = re.search(r'\{.*\}', result.content, re.DOTALL)
    if json_match:
        json_str = json_match.group()
        try:
            extracted_data = json.loads(json_str)
            # Validate with Pydantic model
            validated_data = ExtractedInfo(**extracted_data).model_dump()
            with open(output_path, 'w') as f:
                json.dump(validated_data, f, indent=2)
            print(f"Saved extraction to {output_path}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format for {file_path}")
        except ValueError as e:
            print(f"Error: Data validation failed for {file_path}: {str(e)}")
    else:
        print(f"Error: No JSON found in the output for {file_path}")


# Main processing loop
input_dir = "papers"
output_dir = "extractions/4"  # Changed to extractions/4

os.makedirs(output_dir, exist_ok=True)

for i in range(24, 31):
    if (i == 5 or i == 20):
        continue
    input_path = os.path.join(input_dir, f"p{i}.pdf")
    output_path = os.path.join(output_dir, f"{i}.json")

    print(f"Processing {input_path}...")
    process_pdf(input_path, output_path)

print("All papers processed.")
