import pandas as pd
from pandas_profiling import ProfileReport 

df=pd.read_csv('housing.csv')
print(df)

#Generate report
profile=ProfileReport((df),minimal=True)
profile.to_file(output_file='housing.html')