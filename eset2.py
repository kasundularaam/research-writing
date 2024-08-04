import os
import json
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from llm_lib import llm

# Ensure you have set your OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = "your-api-key"


class MLTechniques(BaseModel):
    algorithms: List[str] = Field(
        description="List of machine learning algorithms used for bug prediction")
    novel_approaches: str = Field(
        description="Novel or hybrid approaches proposed")
    preprocessing: List[str] = Field(
        description="Preprocessing techniques applied to the data")


class SourceLocations(BaseModel):
    ml_techniques: str = Field(
        description="Location of ML techniques information")


class ExtractedInfo(BaseModel):
    ml_techniques: MLTechniques
    source_locations: SourceLocations


parser = PydanticOutputParser(pydantic_object=ExtractedInfo)

prompt_template = """
For the research paper, please extract the following information about machine learning techniques and provide it in a JSON format:
1. Machine Learning Techniques:
   - List all machine learning algorithms used for bug prediction
   - Any novel or hybrid approaches proposed (brief description)
   - Preprocessing techniques applied to the data
For each piece of information, please include the section or page number where it was found in the paper.

{format_instructions}

Please follow these guidelines:
1. In the "algorithms" array, include all machine learning algorithms mentioned for bug prediction, even if they were used as baselines or for comparison.
2. If a novel or hybrid approach is proposed, provide a brief description in the "novel_approaches" field. If none are proposed, use "N/A".
3. In the "preprocessing" array, include all data preprocessing steps mentioned (e.g., feature selection, normalization, handling missing values).
4. If any information is not available or unclear in the paper, please use "N/A" for string values and an empty array [] for list values.
5. In "source_locations", provide the section or page numbers where the information about ML techniques was found.
Please ensure that all relevant machine learning techniques are captured, including traditional algorithms, ensemble methods, and any deep learning approaches if mentioned.

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
output_dir = "extractions/2"  # Changed to extractions/2

os.makedirs(output_dir, exist_ok=True)

for i in range(13, 31):
    if (i == 5 or i == 20):
        continue
    input_path = os.path.join(input_dir, f"p{i}.pdf")
    output_path = os.path.join(output_dir, f"{i}.json")

    print(f"Processing {input_path}...")
    process_pdf(input_path, output_path)

print("All papers processed.")
