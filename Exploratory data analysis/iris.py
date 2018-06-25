import pandas as pd
import matplotlib.pyplot as plt

# Loading Dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris = pd.read_csv(url, names=names)

# Line Plot
iris.plot(x='sepal-length', y='sepal-width')
plt.show()

# Scatter Plot

iris.plot(x='sepal-length', y='sepal-width', kind= 'scatter')
plt.xlabel('sepal length(cm)')
plt.ylabel('sepal width(cm)')
           
plt.show()

# Box Plot

iris.plot(y= 'sepal-width', kind= 'box')
plt.ylabel('sepal width(cm)')
plt.show()

# Histogram

iris.plot(y= 'sepal-length', kind= 'hist')
plt.xlabel('sepal length(cm)')
plt.show()

# More specified histogram
# Here bins= number of intervals, range= extrema of bins(minimum, maximum), normed(boolean)= whether to normalize one


iris.plot(y= 'sepal-length', kind= 'hist', bins=30, range= (4,8), normed= True)
plt.xlabel('sepal length(cm)')
plt.show()

# More specified histogram
# Here cumulative(boolean)= compute cumulative distribution function

iris.plot(y= 'sepal-length', kind= 'hist', bins=30, range= (4,8), cumulative= True, normed= True)
plt.xlabel('sepal length(cm)')
plt.show()

