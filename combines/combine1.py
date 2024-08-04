import json
import os

soq = 5

# Directory containing the JSON files
directory = f'extractions/{soq}/'

# List to store all the combined data
combined_data = []

# Iterate through the files in the directory
for i in range(1, 31):
    if (i == 5 or i == 20):
        continue
    filename = f"{i}.json"
    filepath = os.path.join(directory, filename)

    # Check if the file exists
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            # Load the JSON data
            data = json.load(file)

            # Add the research field to the object
            data['research'] = i

            # Append the modified data to the combined list
            combined_data.append(data)

# Write the combined data to a new JSON file
with open(f'combined/{soq}.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=2)

print(f"Combined JSON file has been created as 'combined/{soq}.json'")
