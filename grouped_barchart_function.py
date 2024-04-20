#grouped_barchart_function.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
