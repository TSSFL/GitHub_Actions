import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#General barcharts
textstr = 'Created at \nwww.tssfl.com'

def plot_grouped_bar_charts(group_names, responses, data):
    fig, ax = plt.subplots(figsize=(10, 10))
    bar_width = 0.1
    opacity = 0.8
    
    colors = ['green', 'crimson', '#00FF00', "#FFD700", 'blue', '#4286f4', "#FF4500"]
    colors = colors[:len(group_names)][::-1]

    total = np.sum(np.sum(data, axis=1))

    for i, group_data in enumerate(data):
        x = np.arange(len(responses))
        bars = ax.barh(x + i * bar_width, group_data, bar_width,
                    alpha=opacity, color=colors[i], label=group_names[i])

        for j, bar in enumerate(bars):
            percentage = '{:.2f}%'.format(100 * bar.get_width() / total)
            frequency = str(int(bar.get_width()))
            y_pos = bar.get_y() + bar.get_height() / 2
            x_pos = bar.get_width()
            ax.annotate(percentage, (x_pos, y_pos), xytext=(12, 0),
                        textcoords="offset points", ha="left", va="center", color='red')

            if x_pos >= 0:
                ax.annotate(frequency, (x_pos, y_pos), rotation=0, xytext=(6, 0),
                            textcoords="offset points", ha="center", va="center", color='green')

    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Responses')
    ax.set_title('Grouped Bar Charts: Frequency and 100% Distribution for Each Group', size=12, pad=20)

    ax.set_yticks(x + (len(group_names) - 1) * bar_width / 2)
    ax.set_yticklabels(responses)

    handles, labels = ax.get_legend_handles_labels()
    legend_bbox = bbox_to_anchor=(1.05, 1)

    plt.gca().legend(handles[::-1], labels[::-1], title="Groups", loc='upper left', bbox_to_anchor=legend_bbox)
    plt.subplots_adjust(right=0.9)

    plt.gcf().text(0.02, 0.95, textstr, fontsize=14, color='green')

    plt.tight_layout()
    plt.show()
    

#Python Class

class GroupedBarCharts:
    def __init__(self):
        pass

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
        
    def create_horizontal_barcharts(self):
        #Call the `plot_grouped_bar_charts` function from the grouped_barchart_function module
        self.plot_grouped_barcharts(group_names, responses, data)

#Create grouped bar charts object and plot
gb = GroupedBarCharts()
       
#Create a random dataframe
group_names = np.random.choice(['Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G'], size=100)
responses = np.random.choice(['agree', 'disagree', 'strongly agree', 'strongly disagree'], size=100)
df = pd.DataFrame({'Column1': group_names, 'Column2': responses})

#Convert dataframe to preserve the original order of responses.
df = pd.crosstab(df['Column1'], df['Column2'])

#Convert pandas dataframe to numpy array
data = df.to_numpy()

#Calculate the total percentage for each group
group_totals = np.sum(data, axis=1)
total = np.sum(group_totals)

#Convert the list to a pandas Series
group_series = pd.Series(group_names)
group_names = group_series.unique()
group_names = group_names[::-1]

response_series = pd.Series(responses)
responses = response_series.unique()

#Call function under class
gb.plot_grouped_barcharts(group_names, responses, data)

#Call imported function
gb.create_horizontal_barcharts()
