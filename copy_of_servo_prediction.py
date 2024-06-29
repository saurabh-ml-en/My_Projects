# -*- coding: utf-8 -*-
"""Copy of servo_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10HAdZF0dfzUF2QMSUfmbODgi9ZC3N_gS
"""

import pandas as pd

df = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Servo%20Mechanism.csv')

df.head()

df.describe()

df.isna().sum()

df.columns

df['Motor'].value_counts()

df['Screw'].value_counts()

df.replace({'Motor':{'A':0,'B':1,'C':2,"D":3,"E":4}}, inplace= True)

df.replace({'Screw':{'A':0,'B':1,'C':2,"D":3,"E":4}}, inplace= True)

y = df['Class']

X= df[['Motor','Screw','Pgain','Vgain']]

y.shape

X.shape

from sklearn.model_selection import train_test_split

X_test,X_train,y_test,y_train = train_test_split(X,y,random_state=2520)

from sklearn.linear_model import LinearRegression
l = LinearRegression()

l.fit(X_train, y_train)

y_p = l.predict(X_test)

l.intercept_

l.coef_

y_p

y_test

from sklearn.metrics import mean_absolute_error,r2_score

mean_absolute_error(y_p,y_test)

r2_score(y_p,y_test)

"""Analyse actual values vs Predicted Values Using Matplotlib"""

import matplotlib.pyplot as plt
plt.scatter(y_test,y_p)
plt.xlabel('Actual value')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted ')
plt.show()

"""**Predicting Using Random One row from Above Dataset**"""

X_new = df.sample(1)

X_new

X_new = X_new.drop(['Class'],axis=1)

X_new

l.predict(X_new)

