import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics as st



df = pd.read_csv("StudentsPerformance.csv")
data = df["math score"].tolist()


mean = sum(data) / len(data)
stddev = st.stdev(data)
median = st.median(data)
mode = st.mode(data)

print("Mean, median,mode of this data is {} ,{} ,{}".format(mean,median,mode))


stddev=st.stdev(data)

print("Standard deviation of this data is {}".format(stddev))


firStdStart,firStdEnd=mean-stddev,mean+stddev
secStdStart,secStdEnd=mean-(2*stddev),mean+(2*stddev)
thrStdStart,thrStdEnd=mean-(3*stddev),mean+(3*stddev)

print("first Standard deviation of this data is {} ,{}".format(firStdStart,firStdEnd))


print("second Standard deviation of this data is {} ,{}".format(secStdStart,secStdEnd))


print("third Standard deviation of this data is {}, {}".format(thrStdStart,thrStdEnd))





listDataInFirDev=[res for res in data if res>firStdStart and firStdEnd>res]
listDataInSecDev=[res for res in data if res>secStdStart and secStdEnd>res]
listDataInThrDev=[res for res in data if res>thrStdStart and thrStdEnd>res]

perc= (len(listDataInFirDev)*100)/len(data)
perc2= (len(listDataInSecDev)*100)/len(data)
perc3= (len(listDataInThrDev)*100)/len(data)

print("percentage of 1st data is {}".format(perc))
print("percentage of 2nd data is {}".format(perc2))
print("percentage of 3rd data is {}".format(perc3))




fig=ff.create_distplot([data],["math scores"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[firStdStart,firStdStart],y=[0,0.17],mode="lines",name="standard dev 1"))
fig.add_trace(go.Scatter(x=[firStdEnd,firStdEnd],y=[0,0.17],mode="lines",name="standard dev 1"))

fig.add_trace(go.Scatter(x=[secStdStart,secStdStart],y=[0,0.17],mode="lines",name="standard dev 2"))
fig.add_trace(go.Scatter(x=[secStdEnd,secStdEnd],y=[0,0.17],mode="lines",name="standard dev 2"))

fig.add_trace(go.Scatter(x=[thrStdStart,thrStdStart],y=[0,0.17],mode="lines",name="standard dev 3"))
fig.add_trace(go.Scatter(x=[thrStdEnd,thrStdEnd],y=[0,0.17],mode="lines",name="standard dev 3"))
fig.show()