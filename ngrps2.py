import matplotlib.pyplot as plt
import pandas as pd
import io

# Function to create a bar plot


def create_bar_plot(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(data.index, data.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

# Function to create a pie chart


def create_pie_chart(data, title, filename):
    plt.figure(figsize=(10, 8))
    plt.pie(data.values, labels=data.index, autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.axis('equal')
    plt.savefig(filename)
    plt.close()


# CSV data for datasets
datasets_csv = '''
Dataset,Number of Studies
NASA MDP,13
PROMISE,13
AEEM,3
Relink,2
Others,4
'''

# CSV data for machine learning techniques
ml_techniques_csv = '''
Technique,Number of Studies
Neural Networks,16
Bayesian Methods,8
Support Vector Machines,4
Random Forests,9
Ensemble Learning,4
Clustering,3
Other,6
'''

# CSV data for software metrics
metrics_csv = '''
Metric Type,Number of Studies
Object-Oriented Metrics,17
Code Complexity Metrics,15
Process Metrics,8
Developer-Related Metrics,6
Semantic Metrics,3
Other,5
'''

# CSV data for performance measures
performance_csv = '''
Measure,Number of Studies
AUC-ROC,23
Precision,18
Recall,17
F1-score,14
Accuracy,12
Other,8
'''

# CSV data for papers published per year
papers_per_year_csv = '''
Year,Number of Papers
2014,5
2015,6
2016,4
2017,3
2018,5
2019,5
2020,3
'''

# Create DataFrames
datasets_df = pd.read_csv(io.StringIO(datasets_csv))
ml_techniques_df = pd.read_csv(io.StringIO(ml_techniques_csv))
metrics_df = pd.read_csv(io.StringIO(metrics_csv))
performance_df = pd.read_csv(io.StringIO(performance_csv))
papers_per_year_df = pd.read_csv(io.StringIO(papers_per_year_csv))

# Set index for easier plotting
datasets_df.set_index('Dataset', inplace=True)
ml_techniques_df.set_index('Technique', inplace=True)
metrics_df.set_index('Metric Type', inplace=True)
performance_df.set_index('Measure', inplace=True)
papers_per_year_df.set_index('Year', inplace=True)

# Create plots
create_bar_plot(datasets_df['Number of Studies'], 'Distribution of Datasets',
                'Dataset', 'Number of Studies', 'datasets_distribution.png')
create_pie_chart(ml_techniques_df['Number of Studies'],
                 'Distribution of Machine Learning Techniques', 'ml_techniques_distribution.png')
create_bar_plot(metrics_df['Number of Studies'], 'Distribution of Software Metrics',
                'Metric Type', 'Number of Studies', 'metrics_distribution.png')
create_bar_plot(performance_df['Number of Studies'], 'Distribution of Performance Measures',
                'Measure', 'Number of Studies', 'performance_measures_distribution.png')
create_bar_plot(papers_per_year_df['Number of Papers'], 'Number of Papers Published per Year',
                'Year', 'Number of Papers', 'papers_per_year.png')

print("Graphs have been generated and saved as PNG files.")
