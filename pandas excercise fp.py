import pandas as pd
movies_df = pd.read_csv("IMDB-Movie-Data2.csv", index_col="Title")
revenue = movies_df['Revenue (Millions)']
revenue.head()

revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace = True)   # alter the values in revenue

metascore_median = movies_df['Metascore'].median()
movies_df['Metascore'].fillna(metascore_median, inplace = True)
print(movies_df.isnull().sum())

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) 
	# set font and plot size to be larger
movies_df.plot(kind='scatter', x='Rating', y='Revenue (Millions)', title='Revenue (millions) vs Rating')


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


