from IPython.display import HTML, display
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd 
import numpy as np
import os

for dirname, _, filenames in os.walk('share-of-students-studying-abroad .csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('share-of-students-studying-abroad .csv')

df.tail()