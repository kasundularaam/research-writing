from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
import markdown
import re
import ast
import json
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the LLM
llm = ChatOpenAI(temperature=0, model_name="gpt-4o",
                 openai_api_key=os.environ.get("OPENAI_API_KEY"))


def read_markdown_file(file_path):
    logging.info(f"Reading file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return markdown.markdown(content)


def extract_qa(html_content):
    logging.info("Extracting Q&A from HTML content")
    start_time = time.time()

    prompt = ChatPromptTemplate.from_template(
        "Extract the questions and answers from the following HTML content. Format the output as a JSON array of objects, where each object has 'question' and 'answer' keys. Do not include any additional formatting or explanation.\n\nContent: {content}\n\nExtracted Q&A:"
    )

    chain = (
        {"content": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    result = chain.invoke(html_content)

    # Remove markdown code block syntax if present
    result = re.sub(r'^```json\s*|\s*```$', '',
                    result.strip(), flags=re.MULTILINE)

    try:
        qa_list = json.loads(result)
        if not qa_list:
            logging.warning(f"No Q&A pairs found in the result: {result}")
    except json.JSONDecodeError as e:
        logging.error(f"JSON parsing error: {e}")
        logging.error(f"Raw result: {result}")
        qa_list = []
    except Exception as e:
        logging.error(f"Unexpected error parsing result: {e}")
        logging.error(f"Raw result: {result}")
        qa_list = []

    end_time = time.time()
    logging.info(f"Q&A extraction completed in {
                 end_time - start_time:.2f} seconds")
    return qa_list


def process_files(directory):
    logging.info(f"Processing files in directory: {directory}")
    all_qa = {}
    file_count = 0
    for filename in os.listdir(directory):
        if filename.startswith("a-") and filename.endswith(".md"):
            file_count += 1
            logging.info(f"Processing file {file_count}: {filename}")
            file_path = os.path.join(directory, filename)
            html_content = read_markdown_file(file_path)
            qa_list = extract_qa(html_content)

            for qa in qa_list:
                question = qa['question']
                answer = qa['answer']
                if question not in all_qa:
                    all_qa[question] = []
                all_qa[question].append((filename, answer))

    logging.info(f"Processed {file_count} files")
    return all_qa


def generate_markdown_files(all_qa, output_directory):
    logging.info(f"Generating output files in directory: {output_directory}")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i, (question, answers) in enumerate(all_qa.items(), 1):
        filename = f"q-{i}.md"
        file_path = os.path.join(output_directory, filename)

        logging.info(f"Writing file: {filename}")
        with open(file_path, 'w', encoding='utf-8') as file:
            for answer_file, answer in answers:
                research_no = answer_file.split('-')[1].split('.')[0]
                file.write(f"# Research {research_no}\n{answer}\n\n")

    logging.info(f"Generated {len(all_qa)} output files")


if __name__ == "__main__":
    start_time = time.time()
    logging.info("Starting the process")

    input_directory = "answers"
    output_directory = "output"

    all_qa = process_files(input_directory)
    generate_markdown_files(all_qa, output_directory)

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Process completed in {total_time:.2f} seconds")
    logging.info(f"Generated {len(all_qa)} markdown files in {
                 output_directory}")
