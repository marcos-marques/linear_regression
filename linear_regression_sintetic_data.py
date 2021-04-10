# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 05:59:22 2021

@author: novom
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Carregando os dados

df_train = pd.read_csv('/Users/novom/Learning/datasets/linear_regression_sintetic_data/train.csv')
df_test = pd.read_csv('/Users/novom/Learning/datasets/linear_regression_sintetic_data/test.csv')

# Preparando os dados

x_train = df_train['x']
y_train = df_train['y']

x_test = df_test['x']
y_test = df_test['y']

x_train = np.array(x_train)
y_train = np.array(y_train)

x_test = np.array(x_test)
y_test = np.array(y_test)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

# Instanciando o modelo
clf = LinearRegression(normalize=True)


# Treinando o modelo
clf.fit(x_train, y_train)

# Predizendo e Avaliando o modelo
y_predicted = clf.predict(x_test)

print(r2_score(y_test, y_predicted))

