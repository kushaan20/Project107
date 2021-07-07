import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('data.csv')
print(df.groupby('level')['attempt'].mean())

fig = px.scatter(df,x = 'student_id',y = 'level',color = 'attempt',title = 'Student Performances', size_minimum = 55, size_max = 60)
fig.show()
