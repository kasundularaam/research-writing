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


class BugPredictionMetric(BaseModel):
    name: str = Field(description="Name of the metric")
    category: str = Field(description="Category of the metric")
    is_novel: bool = Field(description="Whether the metric is novel")
    description: str = Field(
        description="Description of the metric if novel, 'N/A' otherwise")


class SourceLocations(BaseModel):
    bug_prediction_metrics: str = Field(
        description="Location of bug prediction metrics information")


class ExtractedInfo(BaseModel):
    bug_prediction_metrics: List[BugPredictionMetric]
    source_locations: SourceLocations


parser = PydanticOutputParser(pydantic_object=ExtractedInfo)

prompt_template = """
For the research paper titled "{paper_title}", please extract the following information about bug prediction metrics and provide it in a JSON format:
1. Bug Prediction Metrics:
   - List all metrics mentioned for predicting bugs
   - Categorize each metric (e.g., code complexity, process metric, developer metric)
   - Any novel metrics proposed (brief description)
For each piece of information, please include the section or page number where it was found in the paper.

{format_instructions}

Please follow these guidelines:
1. Include all metrics mentioned in the paper, even if they were not the main focus of the study.
2. For each metric, provide:
   - "name": The name of the metric
   - "category": The category it belongs to (e.g., code complexity, process metric, developer metric)
   - "is_novel": Set to true if it's a new metric proposed in this paper, false otherwise
   - "description": A brief description if it's a novel metric, or "N/A" if it's a standard metric
3. If any information is not available or unclear in the paper, please use "N/A" for string values.
4. In "source_locations", provide the section or page numbers where the information about bug prediction metrics was found.
Ensure that all relevant metrics are captured, including both traditional software metrics and any new or adapted metrics proposed for bug prediction.

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

    # Extract paper title from the first page
    paper_title = pages[0].page_content.split(
        '\n', 1)[0] if pages else "Unknown Title"

    result = chain.invoke({
        "format_instructions": parser.get_format_instructions(),
        "paper_content": content,
        "paper_title": paper_title
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
output_dir = "extractions/3"  # Changed to extractions/3

os.makedirs(output_dir, exist_ok=True)

for i in range(1, 31):
    if (i == 5 or i == 20):
        continue
    input_path = os.path.join(input_dir, f"p{i}.pdf")
    output_path = os.path.join(output_dir, f"{i}.json")

    print(f"Processing {input_path}...")
    process_pdf(input_path, output_path)

print("All papers processed.")
