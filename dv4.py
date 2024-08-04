import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from math import pi

# Ensure the directory exists
output_dir = 'dv/4/'
os.makedirs(output_dir, exist_ok=True)

# Load the data from combined/4.json
with open('combined/4.json', 'r') as f:
    data = json.load(f)

# Initialize lists
performance_metrics = []
baseline_models = []
best_models = []
best_models_performance = []

# Extract relevant information
for paper in data:
    performance_metrics.extend(paper['performance_evaluation']['metrics'])
    baseline_models.extend(paper['performance_evaluation']['baseline_models'])
    best_models.append(paper['performance_evaluation']['best_model']['name'])
    best_models_performance.append(
        paper['performance_evaluation']['best_model']['performance'])

# Create DataFrame for performance metrics
df_performance = pd.DataFrame(performance_metrics)
df_baseline = pd.DataFrame({'BaselineModel': baseline_models})
df_best_model_performance = pd.DataFrame(best_models_performance)

# Box Plot: Distribution of performance metrics
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_performance)
plt.title('Distribution of Performance Metrics')
plt.xlabel('Metric')
plt.ylabel('Value')
plt.savefig(os.path.join(output_dir, 'box_plot_performance_metrics.png'))
plt.close()

# Line Chart: Performance trends over time
# Assuming data includes a 'year' field for the trend
years = [paper['year'] for paper in data if 'year' in paper]
performance_over_time = pd.DataFrame({'Year': years, 'Performance': [np.mean(list(
    paper['performance_evaluation']['metrics'].values())) for paper in data if 'metrics' in paper]})
plt.figure(figsize=(12, 6))
sns.lineplot(data=performance_over_time, x='Year', y='Performance', marker='o')
plt.title('Performance Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Average Performance')
plt.savefig(os.path.join(output_dir, 'line_chart_performance_trends.png'))
plt.close()

# Radar Chart: Comparative performance of baseline models vs. best models


def plot_radar_chart(categories, values, title, filename):
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    values += values[:1]
    angles += angles[:1]

    plt.figure(figsize=(8, 8), dpi=100)
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories)
    ax.plot(angles, values, color='red', linestyle='solid',
            linewidth=2, label='Best Model')
    ax.fill(angles, values, color='red', alpha=0.25)

    plt.title(title, size=15, color='red', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()


# Combine best model performance
baseline_performance = [np.mean(df_performance[metric].values)
                        for metric in df_performance.columns]
best_model_performance = [np.mean(list(values.values()))
                          for values in best_models_performance]

# Ensure all metrics are represented
metrics = df_performance.columns.tolist()
plot_radar_chart(metrics, baseline_performance,
                 'Performance Comparison: Baseline vs. Best Models', 'radar_chart_performance_comparison.png')
