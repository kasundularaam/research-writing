import json
import os

# Define input and output directories
input_dir = 'research-data'
output_dir = 'output'
questions_file = 'questions/questions.json'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to read JSON file


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Read questions
questions = read_json(questions_file)

# Process all JSON files
for i in range(1, 31):  # Files are named q1.json, q2.json, ..., q30.json
    json_file = os.path.join(input_dir, f'q{i}.json')
    data = read_json(json_file)

    # Process each question
    for j in range(1, 31):
        question_key = f'question-{j}'
        if question_key in data:
            output_file = os.path.join(output_dir, f'question-{j}.md')

            # Write or append to file
            mode = 'a' if os.path.exists(output_file) and i > 1 else 'w'
            with open(output_file, mode) as file:
                # Write question only once at the top of the file
                if i == 1:
                    file.write(f'# QUESTION\n{questions[question_key]}\n\n')

                file.write(f'# Research {i}\n\n{data[question_key]}\n\n')

print("Processing complete. Check the 'output' folder for results.")
