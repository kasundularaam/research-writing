import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Ensure the directory exists
output_dir = 'dv/2/'
os.makedirs(output_dir, exist_ok=True)

# Load the data from combined/2.json
with open('combined/2.json', 'r') as f:
    data = json.load(f)

# Initialize lists
algorithms = []
novel_approaches = []
preprocessing_techniques = []

# Extract relevant information
for paper in data:
    algorithms.extend(paper['ml_techniques']['algorithms'])
    novel_approaches.append(paper['ml_techniques']['novel_approaches'])
    preprocessing_techniques.extend(paper['ml_techniques']['preprocessing'])

# Create DataFrames for easier manipulation
df_algorithms = pd.DataFrame({'Algorithm': algorithms})
df_novel_approaches = pd.DataFrame({'NovelApproach': novel_approaches})
df_preprocessing = pd.DataFrame({'Preprocessing': preprocessing_techniques})

# Bar Chart: Frequency of different machine learning algorithms
plt.figure(figsize=(12, 6))
sns.countplot(y='Algorithm', data=df_algorithms,
              order=df_algorithms['Algorithm'].value_counts().index)
plt.title('Frequency of Different Machine Learning Algorithms')
plt.xlabel('Count')
plt.ylabel('Algorithm')
plt.savefig(os.path.join(output_dir, 'bar_chart_algorithms.png'))
plt.close()

# Bubble Chart: Relationship between algorithms, novel approaches, and preprocessing techniques
# Create a combined DataFrame
combined_data = []
for paper in data:
    for alg in paper['ml_techniques']['algorithms']:
        for pre in paper['ml_techniques']['preprocessing']:
            combined_data.append({
                'Algorithm': alg,
                'NovelApproach': paper['ml_techniques']['novel_approaches'],
                'Preprocessing': pre
            })
df_combined = pd.DataFrame(combined_data)

plt.figure(figsize=(14, 8))
sns.scatterplot(data=df_combined, x='Algorithm', y='Preprocessing',
                size='NovelApproach', sizes=(20, 200), legend=False)
plt.title(
    'Relationship between Algorithms, Novel Approaches, and Preprocessing Techniques')
plt.xlabel('Algorithm')
plt.ylabel('Preprocessing Technique')
plt.xticks(rotation=90)
plt.savefig(os.path.join(output_dir, 'bubble_chart_relationships.png'))
plt.close()

# Heatmap: Co-occurrence of preprocessing techniques and algorithms
# Create a crosstab DataFrame
crosstab = pd.crosstab(df_combined['Algorithm'], df_combined['Preprocessing'])

plt.figure(figsize=(16, 10))
sns.heatmap(crosstab, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Co-occurrence of Preprocessing Techniques and Algorithms')
plt.xlabel('Preprocessing Technique')
plt.ylabel('Algorithm')
plt.savefig(os.path.join(output_dir, 'heatmap_cooccurrence.png'))
plt.close()
