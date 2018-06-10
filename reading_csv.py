import pandas as pd

# Read the csv file
df1 = pd.read_csv('citiesInFinland.csv')

# Create a list of the new column labels: new_labels
new_labels = ['City','Country']

# Read in the file, specifying the header and names parameters
df2 = pd.read_csv('citiesInFinland.csv', header=0, names=new_labels)

# print the dataframes
print df1
print df2
