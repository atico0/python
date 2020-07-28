import pandas as pd
import datashader as ds
from datashader import transfer_functions as tf
import numpy as np

df = pd.read_csv('/kaggle/input/leagueoflegends/kills.csv')
df.head()
