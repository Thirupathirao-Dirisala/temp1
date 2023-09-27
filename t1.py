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
fig, ax = plt.subplots()
l3=[]
for i in l2:
    l3.append(int(i.split()[0]))
bars=plt.bar(l1 , l3)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
plt.xlabel('Year')
plt.ylabel('Population (M)')
plt.title('Year vs Population')
plt.legend(loc='lower right')
fig
