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


class AdditionalInfo(BaseModel):
    software_domain: str = Field(
        description="Software domain or type focused on in the study")
    limitations: List[str] = Field(
        description="Key limitations or challenges reported in the study")
    future_directions: List[str] = Field(
        description="Future research directions suggested by the authors")


class SourceLocations(BaseModel):
    additional_info: str = Field(
        description="Location of additional information")


class ExtractedInfo(BaseModel):
    additional_info: AdditionalInfo
    source_locations: SourceLocations


parser = PydanticOutputParser(pydantic_object=ExtractedInfo)

prompt_template = """
For the research paper titled "{paper_title}", please extract the following additional information and provide it in a JSON format:
1. Additional Information:
   - Software domain or type focused on in the study
   - Key limitations or challenges reported in the study
   - Future research directions suggested by the authors
For each piece of information, please include the section or page number where it was found in the paper.

{format_instructions}

Please follow these guidelines:
1. For "software_domain", provide a brief description of the type of software or domain focused on in the study (e.g., "web applications", "embedded systems", "mobile apps").
2. In the "limitations" array, list all key limitations or challenges mentioned in the study regarding the bug prediction approach or results.
3. In the "future_directions" array, list all suggestions for future research mentioned by the authors.
4. If any information is not available or unclear in the paper, please use "N/A" for string values and an empty array [] for list values.
5. In "source_locations", provide the section or page numbers where this additional information was found.
Ensure that you capture any significant insights, critiques, or suggestions made by the authors regarding the field of software bug prediction.

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
output_dir = "extractions/5"  # Kept as extractions/3

os.makedirs(output_dir, exist_ok=True)

for i in range(1, 31):
    if (i == 5 or i == 20):
        continue
    input_path = os.path.join(input_dir, f"p{i}.pdf")
    # Changed filename to avoid overwriting
    output_path = os.path.join(output_dir, f"{i}.json")

    print(f"Processing {input_path}...")
    process_pdf(input_path, output_path)

print("All papers processed.")
