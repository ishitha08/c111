import pandas as pd
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('data1.csv')
data = df['Math_score'].tolist()

meanofsample1 = statistics.mean(data)
print('mean of sample 1 -',meanofsample1)

fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
