# -*- coding: utf-8 -*-
#importing the libraries
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

#importing the dataset
#dataset = pd.read_csv('Salary_Data.csv')
#x = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, 1].values

#splitting the dataset into training set and testset
#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""

#fitting simple linear regression to the training set
#from sklearn.linear_model import LinearRegression
#regressor = LinearRegression()
#regressor.fit(x_train, y_train)

#predicting the test set results
#y_pred = regressor.predict(x_test)

#visulising the trining set results
#plt.scatter(x_train, y_train, color = 'red')
#plt.plot(x_train, regressor.predict(x_train), color = 'blue')
#plt.title('Salary vs Experience (Training set)')
#plt.xlabel('Years of Experience')
#plt.ylabel('Salary')
#plt.show()  #to specify it is end of graph

#plt.scatter(x_test, y_test, color = 'red')
#plt.plot(x_train, regressor.predict(x_train), color = 'blue')
#plt.title('Salary vs Experience (Test set)')
#plt.xlabel('Years of Experience')
#plt.ylabel('Salary')
#plt.show() 
