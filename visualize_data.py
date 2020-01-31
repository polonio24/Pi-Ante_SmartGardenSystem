import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('freewilly_data.csv',sep='\t')

print(df.columns)
df.plot(x='dataora',y=['temperature','humidity','soilMoisture','tankPCFull'])
plt.show()