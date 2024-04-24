import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import requests
from importlib.machinery import SourceFileLoader
import io

textstr = 'Created at \nwww.tssfl.com'

#Download the grouped_barchart_function.py file from GitHub
url = 'https://raw.githubusercontent.com/username/repo/main/grouped_barchart_function.py'
download = requests.get(url).text

#Write the downloaded content to a temporary file
with open('grouped_barchart_function.py', 'w') as file:
    file.write(download)

#Import the function from the downloaded file
temporary_module = SourceFileLoader('grouped_barchart_module', 'grouped_barchart_function.py').load_module()
plot_grouped_bar_charts = temporary_module.plot_grouped_bar_charts

