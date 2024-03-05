import pandas as pd
import matplotlib.pyplot as pl

def read_csv(csv_file):
    try:
        df=pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        print("File doesn't exist. Please provide the right path.")
        return None
    except Exception as e:
        print(f"message:{e}")
        return None

def generate_report(data):
    # This segregate from non-numeric so that there won't be any future errors  
    data_report=data.select_dtypes(include=['number']).describe()
    # Transpose makes the table more readable by swapping the rows and colmn headers
    data_transpose=data_report.T
    return data_transpose

def generate_histogram(df,column):
    data=df[column]
    pl.figure(figsize=(8,6))
    pl.hist(data,bins=20,color="skyblue",edgecolor="black")
    pl.title(f"Histogram of {column}")
    pl.xlabel(column)
    pl.ylabel('Frequency')
    pl.show()

def generate_boxplot(df,column):
    data=df[column]
    pl.figure(figsize=(10,5))
    pl.boxplot(data,vert=False)
    pl.title(f"Boxplot of the {column}")
    pl.xlabel(column)
    pl.grid(True)
    pl.show()

def generate_scatterplot(data,x_column,y_column):
    x_data=data[x_column]
    y_data=data[y_column]
    
    pl.figure(figsize=(8,6))
    pl.scatter(x_data,y_data,color='blue',alpha=0.5)
    pl.xlabel(x_column)
    pl.ylabel(y_column)
    pl.show()
    

# The file I'm generate report of 
csv_file="BestLap.csv"
df=read_csv(csv_file)
# This drops/deletes anything that has empty values and then reset_index reassigns the sr no. of the element/data 
cleansed_data=df.dropna().reset_index(drop=True)
cleansed_data.groupby("aggregateRating/ratingValue").max()
cleansed_data.groupby("aggregateRating/ratingValue").count()
print(generate_report(cleansed_data))
generate_histogram(cleansed_data,"aggregateRating/ratingValue")
generate_boxplot(cleansed_data,"aggregateRating/ratingValue")
generate_scatterplot(cleansed_data,"aggregateRating/ratingValue","aggregateRating/reviewCount")



