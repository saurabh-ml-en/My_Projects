# -*- coding: utf-8 -*-
"""winemulticlassification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F6_tuMmAjyPIeHouTZHkL38Xy1eYBsC7
"""

import pandas as pd

df= pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Wine.csv')

df.head()

df.tail()

df.columns

y = df['class_name']

x = df.drop(['class_label','class_name'],axis=1)

x.shape

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=2529)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=500)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

from sklearn.metrics import accuracy_score, classification_report

accuracy_score(y_test,y_pred)

classification_report(y_pred,y_test)