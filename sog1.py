import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON data
with open('combined/1.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(data)

# 1. Bar chart: Frequency of dataset names used across studies
plt.figure(figsize=(12, 6))
dataset_counts = df['dataset.name'].explode().value_counts()
dataset_counts.plot(kind='bar')
plt.title('Frequency of Dataset Names Used Across Studies')
plt.xlabel('Dataset Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('dataset_frequency.png')
plt.close()

# 2. Pie chart: Distribution of programming languages in datasets
plt.figure(figsize=(10, 10))
language_counts = df['dataset.language'].explode().value_counts()
plt.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Programming Languages in Datasets')
plt.axis('equal')
plt.savefig('language_distribution.png')
plt.close()

# 3. Scatter plot: Dataset size vs. publication year
plt.figure(figsize=(12, 6))
# Function to safely convert dataset size to float


def safe_float(x):
    if x and isinstance(x, list) and x[0]:
        try:
            return float(x[0])
        except ValueError:
            return None
    return None


df['dataset_size'] = df['dataset.size'].apply(safe_float)
# Remove rows where dataset_size or year is None
df_scatter = df.dropna(subset=['dataset_size', 'paper_info.year'])
plt.scatter(df_scatter['paper_info.year'], df_scatter['dataset_size'])
plt.title('Dataset Size vs. Publication Year')
plt.xlabel('Publication Year')
plt.ylabel('Dataset Size')
plt.savefig('dataset_size_vs_year.png')
plt.close()

# 4. Stacked bar chart: Dataset sources by year
plt.figure(figsize=(12, 6))
# Explode the 'dataset.source' column and count occurrences
source_by_year = df.explode('dataset.source').groupby(
    ['paper_info.year', 'dataset.source']).size().unstack(fill_value=0)
sns.set(style="whitegrid")
source_by_year.plot(kind='bar', stacked=True)
plt.title('Dataset Sources by Year')
plt.xlabel('Publication Year')
plt.ylabel('Count')
plt.legend(title='Source', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('dataset_sources_by_year.png')
plt.close()

print("All graphs have been generated and saved.")
