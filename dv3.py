import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import squarify  # for treemap

# Ensure the directory exists
output_dir = 'dv/3/'
os.makedirs(output_dir, exist_ok=True)

# Load the data from combined/3.json
with open('combined/3.json', 'r') as f:
    data = json.load(f)

# Initialize lists
metric_names = []
categories = []
novelties = []
descriptions = []

# Extract relevant information
for paper in data:
    for metric in paper['bug_prediction_metrics']:
        metric_names.append(metric['name'])
        categories.append(metric['category'])
        novelties.append(metric['is_novel'])
        descriptions.append(metric['description'])

# Create DataFrames for easier manipulation
df_metrics = pd.DataFrame({
    'Metric': metric_names,
    'Category': categories,
    'Novelty': novelties,
    'Description': descriptions
})

# Bar Chart: Frequency of different metrics
plt.figure(figsize=(12, 6))
sns.countplot(y='Metric', data=df_metrics,
              order=df_metrics['Metric'].value_counts().index)
plt.title('Frequency of Different Metrics')
plt.xlabel('Count')
plt.ylabel('Metric')
plt.savefig(os.path.join(output_dir, 'bar_chart_metrics.png'))
plt.close()

# Pie Chart: Proportion of novel vs. standard metrics
novelty_counts = df_metrics['Novelty'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(novelty_counts, labels=['Standard',
        'Novel'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Novel vs. Standard Metrics')
plt.savefig(os.path.join(output_dir, 'pie_chart_novelty.png'))
plt.close()

# Treemap: Distribution of metrics by category
category_counts = df_metrics['Category'].value_counts()
plt.figure(figsize=(12, 8))
squarify.plot(sizes=category_counts, label=category_counts.index, alpha=.8)
plt.title('Distribution of Metrics by Category')
plt.axis('off')
plt.savefig(os.path.join(output_dir, 'treemap_categories.png'))
plt.close()
