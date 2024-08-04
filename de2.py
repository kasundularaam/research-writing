import json
import os

# Input and output file paths
input_file = 'combined/2.json'
output_file = 'combined/2/preprocessing.json'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Load data from file
with open(input_file, 'r') as f:
    data = json.load(f)

# Initialize the result list
result = []

# Process each JSON object in the original data
for item in data:
    # Extract datasets and research ID from the current item
    datasets = item['ml_techniques']['preprocessing']
    research_id = item['research']

    # Create a new entry for each item
    result.append({
        "research": research_id,
        "preprocessing": datasets
    })

# Save result to file
with open(output_file, 'w') as f:
    json.dump(result, f, indent=2)

print(f"Dataset information has been saved to {output_file}")
