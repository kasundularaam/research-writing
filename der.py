import json
import os

# Input and output file paths
input_file = 'combined/1.json'
dataset_file = 'combined/1/dataset.json'
output_file = 'combined/1/updated.json'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Load original data
with open(input_file, 'r') as f:
    original_data = json.load(f)

# Load dataset data
with open(dataset_file, 'r') as f:
    dataset_data = json.load(f)

# Create a dictionary for quick lookup of datasets by research ID
dataset_lookup = {item['research']: item['dataset'] for item in dataset_data}

# Update the original data with new dataset name fields
for item in original_data:
    research_id = item['research']
    if research_id in dataset_lookup:
        item['dataset']['name'] = dataset_lookup[research_id]
    else:
        print(f"Warning: No dataset found for research ID {research_id}")

# Save updated data to file
with open(output_file, 'w') as f:
    json.dump(original_data, f, indent=2)

print(f"Updated data has been saved to {output_file}")
