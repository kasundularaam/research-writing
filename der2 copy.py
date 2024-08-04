import json
import os

# Input and output file paths
original_file = 'combined/4.json'
algorithms_file = 'combined/4/metrics.json'
output_file = 'combined/4/update.json'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Load original data
with open(original_file, 'r') as f:
    original_data = json.load(f)

# Load algorithms data
with open(algorithms_file, 'r') as f:
    algorithms_data = json.load(f)

# Create a dictionary for quick lookup of algorithms by research ID
algorithms_lookup = {item['research']: item['preprocessing']
                     for item in algorithms_data}

# Update the original data with new algorithms
for item in original_data:
    research_id = item['research']
    if research_id in algorithms_lookup:
        item['ml_techniques']['preprocessing'] = algorithms_lookup[research_id]
    else:
        print(f"Warning: No preprocessing found for research ID {research_id}")

# Save updated data to file
with open(output_file, 'w') as f:
    json.dump(original_data, f, indent=2)

print(f"Updated data has been saved to {output_file}")
