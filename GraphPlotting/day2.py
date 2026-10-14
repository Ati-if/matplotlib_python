import numpy as np
import pandas as  pd 

df = pd.DataFrame(np.random.randn(6 , 4) , index = list(range (1 , 7)) , columns = list("ABCD"))
print(df)






print(df.describe())












from matplotlib import pylab

print(pylab.__version__)












#Use matplotlib to import random data

import numpy as np

x = np.linspace(0 , 5 , 10)

y = x * x + 2 

print(x)
print(y)