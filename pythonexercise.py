# import libraries
from subprocess import check_output
import numpy as np # linear algebra
import pandas as pd # data processing
import warnings 
warnings.filterwarnings('ignore') #ignore warnings
from math import ceil 

#Visualization
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.metrics import confusion_matrix #Confusion matrix
from sklearn.metrics import accuracy_score # Accuracy score

# Spliting training and testing
from sklearn.model_selection import train_test_split

#Advanced optimization
from scipy import optimize as op

# Loading the data
data_iris=pd.read_csv('C:/Users/Dominick/Documents/My Documents/Education/Pluralsight-LinkedIn/Intermediate_Python/Iris.csv') # Enter the path of the directory where input csv is stored
#C:\Users\Dominick\Documents\My Documents\Education\Pluralsight-LinkedIn\Intermediate_Python
#print(data_iris.head()) # first 5 entries of the dataset
#print(data_iris.info())
#print(data_iris.describe())
#print(data_iris.isnull().values.any())
print('Iris-setosa')
setosa = data_iris['Species'] == 'Iris-setosa'
print(data_iris[setosa].describe())
print('\nIris-versicolor')
versicolor = data_iris['Species'] == 'Iris-versicolor'
print(data_iris[versicolor].describe())
print('\nIris-virginica')
virginica = data_iris['Species'] == 'Iris-virginica'
print(data_iris[virginica].describe())
# The Histogram representation of the univariate plots for each measurement

np = data_iris.drop('Id', axis=1) # dropping the Id 
np.hist(edgecolor='blue', linewidth=1.2)
fig=plt.gcf()
fig.set_size_inches(12,6)
plt.show()


# ploting scatter plot with respect to petal length

petalPlt = sb.FacetGrid(data_iris, hue="Species", size=6).map(plt.scatter, "PetalLengthCm", "PetalWidthCm")
plt.legend(loc='upper left');
plt.title("Petal Length VS Width");


# Plotting scatter plot with respect to sepal length
sepalPlt = sb.FacetGrid(data_iris, hue="Species", size=6).map(plt.scatter, "SepalLengthCm", "SepalWidthCm")
plt.legend(loc='upper right');
plt.title("Sepal Length VS Width")
# Using seaborn pairplot to see the bivariate relation between each pair of features

import seaborn as sns
sns.set_palette('husl')

nl = data_iris.drop('Id', axis=1) # dropping the Id 
b = sns.pairplot(nl,hue="Species",diag_kind="kde", markers='+',size =3 );
plt.show()

# Data setup
import numpy as np
Species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# Number of examples
m = data_iris.shape[0]
# Features
n = 4
# Number of classes
k = 3

X = np.ones((m,n + 1))
y = np.array((m,1))
X[:,1] = data_iris['PetalLengthCm'].values
X[:,2] = data_iris['PetalWidthCm'].values
X[:,3] = data_iris['SepalLengthCm'].values
X[:,4] = data_iris['SepalWidthCm'].values

# Labels
y = data_iris['Species'].values

# Mean normalization
for j in range(n):
    X[:, j] = (X[:, j] - X[:,j].mean())
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 11)
# it shows 80% of data is split for training and 20% of the data goes to testing.

X = data_iris.drop(['Id', 'Species'], axis=1)
y = data_iris['Species']
# print(X.head())
print(X_train.shape)
# print(y.head())
print(y_test.shape)