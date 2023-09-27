import pandas as pd
import js
import matplotlib.pyplot as plt

r=js.localStorage.getItem('myValue')
from pyodide.http import open_url
url = 'https://raw.githubusercontent.com/Boddudinesh/automation/main/SEM-3.2.csv'
df = pd.read_csv(open_url(url))
x=df.loc[df["REDG NO"] == r]
d = x.to_dict(orient='records')
l1 = list(d[0].keys())[4:]
l2 = list(d[0].values())[4:]

l3=[]
for i in l2:
    l3.append(int(i.split()[0]))
fig, ax = plt.subplots()  # Use subplots to create a figure and axis

ax.bar(l1, l3)

# Display the figure
plt.show()
fig
