import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Ensure the directory exists
output_dir = 'dv/1/'
os.makedirs(output_dir, exist_ok=True)

# Load the data from 1.json
with open('combined/1.json', 'r') as f:
    data = json.load(f)

# Initialize lists
dataset_names = []
dataset_sizes = []
dataset_sources = []
dataset_languages = []

# Extract relevant information ensuring equal lengths
for paper in data:
    names = paper['dataset']['name']
    sizes = paper['dataset']['size']
    sources = paper['dataset']['source']
    languages = paper['dataset']['language']

    min_length = min(len(names), len(sizes), len(sources), len(languages))

    dataset_names.extend(names[:min_length])
    dataset_sizes.extend(sizes[:min_length])
    dataset_sources.extend(sources[:min_length])
    dataset_languages.extend(languages[:min_length])

# Create a DataFrame for easier manipulation
df = pd.DataFrame({
    'Name': dataset_names,
    'Size': dataset_sizes,
    'Source': dataset_sources,
    'Language': dataset_languages
})

# Bar Chart: Number of papers using each dataset
plt.figure(figsize=(10, 6))
sns.countplot(y='Name', data=df, order=df['Name'].value_counts().index)
plt.title('Number of Papers Using Each Dataset')
plt.xlabel('Count')
plt.ylabel('Dataset Name')
plt.savefig(os.path.join(output_dir, 'bar_chart.png'))
plt.close()

# Pie Chart: Proportion of datasets based on their source
source_counts = df['Source'].value_counts()

# Group categories below 3.5% under 'Others'
threshold = 0.035
total = source_counts.sum()
others = source_counts[source_counts / total < threshold]
source_counts = source_counts[source_counts / total >= threshold]
source_counts['Others'] = others.sum()

plt.figure(figsize=(8, 8))
plt.pie(source_counts, labels=source_counts.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Datasets by Source')
plt.savefig(os.path.join(output_dir, 'pie_chart.png'))
plt.close()

# Box Plot: Distribution of dataset sizes
plt.figure(figsize=(10, 6))
sns.boxplot(x='Size', data=df)
plt.title('Distribution of Dataset Sizes')
plt.xlabel('Dataset Size')
plt.savefig(os.path.join(output_dir, 'box_plot.png'))
plt.close()

# Stacked Bar Chart: Languages used in datasets across different papers
language_counts = df.groupby(
    'Name')['Language'].value_counts().unstack().fillna(0)
language_counts.plot(kind='bar', stacked=True, figsize=(12, 7))
plt.title('Languages Used in Datasets Across Different Papers')
plt.xlabel('Dataset Name')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'stacked_bar_chart.png'))
plt.close()
