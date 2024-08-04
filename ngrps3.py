import matplotlib.pyplot as plt
import pandas as pd
import io

# Function to create a bar plot


def create_bar_plot(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.index, data.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height}',
                 ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


# CSV data for research platforms
platforms_csv = '''
Platform,Number of Studies
Google Scholar,6
IEEE Xplore,6
Research Gate,4
ScienceDirect,8
SpringerLink,6
'''

# Create DataFrame
platforms_df = pd.read_csv(io.StringIO(platforms_csv))

# Set index for easier plotting
platforms_df.set_index('Platform', inplace=True)

# Create plot
create_bar_plot(platforms_df['Number of Studies'], 'Distribution of Research Platforms',
                'Platform', 'Number of Studies', 'research_platforms_distribution.png')

print("Graph has been generated and saved as research_platforms_distribution.png")
