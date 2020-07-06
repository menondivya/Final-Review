import pandas as pd
#convert csv's to line protocol

#convert sample data to line protocol (with nanosecond precision)
df = pd.read_csv("Example7.csv")
lines = ["flame" + " "
         + "Building1Flame=" + str(df["Building1Flame"][d]) + ","
         + "Building2Flame=" + str(df["Building2Flame"][d]) + ","
         + "Building3Flame=" + str(df["Building3Flame"][d]) + ","
         + "Building4Flame=" + str(df["Building4Flame"][d]) + ","
         + "Building5Flame=" + str(df["Building5Flame"][d]) 
	 + " " + str(df["xvalue"][d]) for d in range(len(df))]

thefile = open('chronograf.txt', 'w')
for item in lines:
    thefile.write("%s\n" % item)
