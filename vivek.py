# -*- coding: utf-8 -*-
"""Vivek.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ykCRgHXQ4Q4heL2Fij6rn6TPIdmNpJiS
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression  
from sklearn import metrics  
from sklearn.metrics import r2_score
# %matplotlib inline

# Importing the dataset
df = pd.read_csv('/content/drive/My Drive/vivek/dataset.csv')
df.head(12)

df.isna().any()

# Visualizing the given data into a plot.
plt.figure(figsize=(15, 8), facecolor='red')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.scatter(df['Hours'], df['Scores'], label = "datapoints", color = "blue")  
plt.title('Hours Studied vs Percentage Scored')  
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score')  
plt.grid()
plt.legend()
plt.show()
print('From the above plot, it can be deduced that there is a clear positive relation between the variables Hours Studied and Percentage Score')

# Spliting the data into attributes and labels
X = df.iloc[:, :-1].values #Input value to linearRegression is a 2D array 
Y = df.iloc[:, 1].values
X[:5]

Y[:5]

# Splitting the dataset into training and test sets and then train the model with training set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
linearRegression = LinearRegression()  
linearRegression.fit(X_train, Y_train) 
print("Training the model is completed")

#Create a regression line for the train data
data_line = linearRegression.coef_*X+linearRegression.intercept_

# Plot the data around regression line
plt.figure(figsize=(7, 4), facecolor='red')
plt.xlim(0, 10)
plt.ylim(0, 100)
plt.scatter(X, Y, label = "Data Points", color = "blue")
plt.plot(X, data_line, label = "Regression line", color = "black")
plt.title("Linear Regression line for the data")
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score') 
plt.grid()
plt.legend()
plt.show()

Y_pred = linearRegression.predict(X_test) # Predicting the scores

# Tabulate actual and predicted values of test set
pred_data = pd.DataFrame(list(zip(Y_test, Y_pred)),columns=['Actual','Predicted']) 
pred_data.head()

# Plot Predicted values against Actual data to visualize the difference
plt.figure(figsize=(7, 4), facecolor='red')
plt.xlim(0, 10)
plt.ylim(0, 100)

plt.scatter(X_test, Y_test, c='orange',  label='Actual data')
plt.scatter(X_test, Y_pred, c='blue',  label='Predicted values')
plt.plot(X, data_line, label = "Regression line", color = "yellow")

plt.title("Plot of predicted vs actual data")
plt.xlabel('Hours Studied')  
plt.ylabel('Percentage Score') 
plt.grid()
plt.legend()
plt.show()

# Evaluating the model
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred)) 
print('r2 score           : {}'.format(r2_score(Y_test, Y_pred)))

print('Question: Find percent if number of hours = 9.25')
hours = 9.25
number_of_hours = linearRegression.predict([[hours]])
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(number_of_hours[0]))