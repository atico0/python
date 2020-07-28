import pandas as pd
import numpy as np
np.random.seed(101)
a = ['a','b','c']
c = pd.Series(index=a)
df = pd.DataFrame(np.arange(0,20).reshape(5,4), index= 'A B C D E'.split(), columns= 'W X Y Z'.split())
print(df)
print(df['W'])
