import csv
import pandas as pd
import random
import statistics as s
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("tem.csv")
data = df["temp"].to_list()
population_mean = s.mean(data)
population_standrad_div = s.stdev(data)
# fig = ff.create_distplot([data],["temp"],show_hist = False)
# fig.show()
# print(population_mean)
# print(population_standrad_div)

# data_set = []
# for i in range(0,1000):
#    random_index = random.randint(0,len(data))
#    value = data[random_index]
#    data_set.append(value)
# data_mean = s.mean(data_set)
# data_stdiv = s.stdev(data_set)
# # print(data_mean)
# # print(data_stdiv)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
       random_index = random.randint(0,len(data))
       value = data[random_index]
       data_set.append(value)
    data_mean = s.mean(data_set)
    return data_mean

def show_fig(mean_list):
    df = mean_list
    mean = s.mean(mean_list)
    stdiv = s.stdev(mean_list)
    fig = ff.create_distplot([df],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1], mode = "lines",name = "MEAN"))
    fig.show()
    print(mean)
    print(stdiv)

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)


setup()