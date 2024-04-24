import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GroupedBarCharts:
    def __init__(self, function_url):
        self.function_url = function_url
        self.function_script = requests.get(self.function_url).text

        exec(self.function_script, globals())

    def plot_grouped_barcharts(self, group_names, responses, data):
        fig, ax = plt.subplots(figsize=(14, 7))
        bar_width = 0.1
        opacity = 0.8
        total = np.sum(np.sum(data, axis=1))
        colors = ['green', 'crimson', '#00FF00', "#FFD700", 'blue', '#4286f4', "#FF4500"]

        for i, group_data in enumerate(data):
            x = np.arange(len(responses))
            bars = ax.bar(x + i * bar_width, group_data, bar_width,
                          alpha=opacity, color=colors[i], label=group_names[i], align='edge')

            for j, bar in enumerate(bars):
                percentage = '{:.2f}%'.format(100 * bar.get_height() / total)
                frequency = str(int(bar.get_height()))
                x_pos = bar.get_x() + bar.get_width() / 2
                y_pos = bar.get_height()
                ax.annotate(percentage, (x_pos, y_pos), rotation=90, xytext=(0, 15),
                            textcoords="offset points", ha="center", va="bottom", color='red')
                if y_pos >= 0:
                    ax.annotate(frequency, (x_pos, y_pos), rotation=0, xytext=(0, 7),
                                textcoords="offset points", ha="center", va="center", color='green')

        ax.spines['top'].set_visible(False)
        ax.set_xlabel('Responses')
        ax.set_ylabel('Frequency')
        ax.set_title('Grouped Bar Charts: Frequency and 100% Distribution Across Groups', size=12, pad=40)
        ax.set_xticks(x + (len(group_names) - 1) * bar_width / 2)
        ax.set_xticklabels(responses)

        legend = plt.legend(title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.subplots_adjust(right=0.9)
        plt.tight_layout()
        plt.show()

    def create_barchart(self, group_names, responses, data):
        plot_grouped_bar_charts(group_names, responses, data)

# Specify the URL of the function script on GitHub
function_url = 'https://raw.githubusercontent.com/TSSFL/GitHub_Actions/master/grouped_barchart_function.py'

# Create grouped bar charts object and plot
gb = GroupedBarCharts(function_url)

# Generate random data for testing
group_names = np.random.choice(['Group A', 'Group B', 'Group C', 'Group D'], size=100)
responses = np.random.choice(['agree', 'disagree', 'strongly agree', 'strongly disagree'], size=100)
df = pd.DataFrame({'Column1': group_names, 'Column2': responses})
df = pd.crosstab(df['Column1'], df['Column2'])
data = df.to_numpy()

# Convert the list to a pandas Series
group_series = pd.Series(group_names)
group_names = group_series.unique()
group_names = group_names[::-1]

response_series = pd.Series(responses)
responses = response_series.unique()

# Call the plot_grouped_barcharts method
gb.plot_grouped_barcharts(group_names, responses, data)

# Call the create_barchart method to use the external function
gb.create_barchart(group_names, responses, data)
