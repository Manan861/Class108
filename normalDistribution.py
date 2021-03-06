import csv 
import pandas as pd
import plotly.express as px 
import plotly.figure_factory as ff

df=pd.read_csv("HeightWeight.csv")
fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"], show_hist=False)

fig.show()