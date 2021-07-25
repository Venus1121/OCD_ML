import matplotlib as mpl

import pandas as pd
import matplotlib.pyplot as plt

mpl.use('AGG')

df=pd.read_csv('Metrocal_WL260_4DOF_Az45_10w.csv')
data=df.iloc[0,5:].tolist()

plt.subplots(4,4,figsize=(9,9))

for i in range(16):
    plt.subplot(4,4,i+1)
    plt.plot(data[i*109:(i+1)*109])


plt.savefig("11.png")