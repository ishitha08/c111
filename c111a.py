import pandas as pd
import random
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()



mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print('mean-',mean)
print('std_deviation',std_deviation)

def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print('mean for sample distribution',mean)
print('std_deviation for sample distribution -',std_deviation)

fig = ff.create_distplot([data],['Math Scores'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = 'lines',name = 'mean'))
fig.show()

df = pd.read_csv('data1.csv')
data = df['Math_score'].tolist()

meanofsample1 = statistics.mean(data)
print('mean of sample 1 -',meanofsample1)

fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)


