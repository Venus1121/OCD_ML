import pandas as pd
from tqdm import tqdm
import os


PATH = 'Metrocal_WL260_4DOF_Az45_10w.csv'
chunksize = 500

i=0
for df_chunk in tqdm(pd.read_csv(PATH, chunksize=chunksize)):
    filename='0'*(6-len(str(i)))+str(i)+'.csv'
    df_chunk.to_csv('./Metrocal/{}'.format(filename))
    i+=1
