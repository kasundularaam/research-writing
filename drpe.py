import os
import json
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
from llm_lib import llm

# Ensure you have set your OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = "your-api-key"


class PaperInfo(BaseModel):
    title: str = Field(description="Title of the paper")
    year: Optional[int] = Field(description="Publication year")
    doi: str = Field(description="DOI of the paper")


class Dataset(BaseModel):
    name: List[str] = Field(description="Names of datasets used")
    size: List[Optional[int]] = Field(description="Sizes of datasets")
    source: List[str] = Field(description="Sources of datasets")
    language: List[str] = Field(
        description="Programming languages of the software in the datasets")


class SourceLocations(BaseModel):
    paper_info: str = Field(description="Location of paper information")
    dataset: str = Field(description="Location of dataset information")


class ExtractedInfo(BaseModel):
    paper_info: PaperInfo
    dataset: Dataset
    source_locations: SourceLocations


parser = PydanticOutputParser(pydantic_object=ExtractedInfo)

prompt_template = """
Extract the following information from the research paper and provide it in a JSON format:
1. Paper Information:
   - Title of the paper
   - Publication year
   - DOI (if available)
2. Dataset Information:
   - Name(s) of dataset(s) used
   - Size of each dataset (number of instances, if provided)
   - Source of each dataset (e.g., open-source project, proprietary)
   - Programming language(s) of the software in the dataset
For each piece of information, include the section or page number where it was found in the paper.

{format_instructions}

If any information is not available or unclear in the paper, use "N/A" for string values and null for numeric values.
Ensure that all fields in the "dataset" object are arrays, even if there's only one dataset.

Here is the content of the research paper:
{paper_content}

Provide the extracted information in the specified JSON format.
"""

# Create LLM chain

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
output_dir = "extractions/1"

os.makedirs(output_dir, exist_ok=True)

for i in range(21, 31):
    if (i != 22):
        continue

    input_path = os.path.join(input_dir, f"p{i}.pdf")
    output_path = os.path.join(output_dir, f"{i}.json")

    print(f"Processing {input_path}...")
    process_pdf(input_path, output_path)

print("All papers processed.")
