from distutils.version import LooseVersion
from re import A
import pandas as pd
from pandas.core.reshape.pivot import pivot_table
import plotly.figure_factory as pff
import statistics as st
import random

data = pd.read_csv("../CSVFiles/medium_data.csv")
claps = data["claps"].tolist()
List = []
def dataSampling():
    for x in range(0,100):
        temp = random.randint(0,len(claps)-1)
        val = claps[temp]
        List.append(val)
    
    Samplemean = st.mean(List)
    return Samplemean

MeanList = []
for i in range(0,1000):
    val = dataSampling()
    MeanList.append(val)

standardDv = st.stdev(claps)
SamplestandardDv = st.stdev(MeanList)
print(SamplestandardDv , standardDv)

graph = pff.create_distplot([claps], ["Random Data"] , show_hist = False)
graph.show()
graph2 = pff.create_distplot([MeanList] , ["RandomDATA"] , show_hist = False)
graph2.show()