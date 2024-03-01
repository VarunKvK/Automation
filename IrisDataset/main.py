import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pt

dt= pd.read_csv("IRIS.csv")
clean_dt=dt.dropna()


# Exclude the non-numeric values from the datset for prper correlation
# This is to give us the header of the data in the iris dataset
numeric_column= clean_dt.select_dtypes(include=['number']).columns

# This gives us the values of the iris dataset 
numeric_data=clean_dt[numeric_column]
# print(numeric_data)

# Correlation Matrix of the data
cor_dat=numeric_data.corr()

pt.figure(figsize=(8,6))
sns.heatmap(cor_dat,annot=True,cmap="coolwarm",fmt=".2f",linewidths=0.5)
pt.title("Correlation Matrix")
pt.show()
