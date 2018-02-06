# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# Dimensions of data set
print('Dimension : '+str(dataset.shape))

# Peek at the data - first 20 rows
print(dataset.head(20))

# Statistical summary - count, mean, the min and max values
print(dataset.describe())

# Class distribution
print(dataset.groupby('class').size())

# Visualization - Univariate plots
# box and whisker plots
dataset.plot(kind = 'box', subplots = True, layout = (2,2), sharex = False, sharey=False)
#plt.show()

# histogram
dataset.hist()
#plt.show()

# Visualization - Multivariate plots
scatter_matrix(dataset)
plt.show()