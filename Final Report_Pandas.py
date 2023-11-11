# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:43:12 2022

@author: ACER
"""

import pandas as pd
dss_df = pd.read_csv("ds_salaries.csv", index_col="job_title")

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) 
	# set font and plot size to be larger
dss_df.plot(kind='scatter', x='work_year', y='salary', title='work year vs salary')
dss_df.plot(kind='scatter', x='work_year', y='salary_in_usd', title='work year vs salary in usd')

dss_df['salary'].plot(kind='hist', title='salary')

dss_df['salary'].plot(kind='box', title= 'salary')

dss_df['salary'].describe()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df2.plot.bar();
df2.plot.bar(stacked=True)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
data.plot.pie(figsize=(6, 6));

