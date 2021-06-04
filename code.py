
import random 
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd


df=pd.read_csv("StudentsPerformance.csv")
data=df["math score"].tolist()

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
sd=statistics.stdev(data)
print("Mean",mean)
print("Median",median)
print("Mode",mode)
print("Sd",sd)




#Sd Start
first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)

fig=ff.create_distplot([data],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION ONE"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION TWO"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.2],mode="lines",name="STANDARD DEVIATION THIRD"))
fig.show()
list_of_data_sd_first=[result for result in data if result>first_sd_start and result<first_sd_end]
list_of_data_sd_second=[result for result in data if result>second_sd_start and result<second_sd_end]
list_of_data_sd_third=[result for result in data if result>third_sd_start and result<third_sd_end]

print("{}% of data lies within 1 std".format(len(list_of_data_sd_first)*100/len(data)))
print("{}% of data lies within 2 std".format(len(list_of_data_sd_second)*100/len(data)))
print("{}% of data lies within 3 std".format(len(list_of_data_sd_third)*100/len(data)))
