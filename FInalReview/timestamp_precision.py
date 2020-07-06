import pandas as pd
# import csv
df = pd.read_csv('Example7.csv')
df.head()
# convert minute precision to nanosecond precision
df["xvalue"] = [str(df["xvalue"][t]) + "000000000" for t in range(len(df))]
df.head()
# export as csv
ns_precision = df
ns_precision.to_csv('data_ns.csv', index=False)
