# -*- coding: utf-8 -*-
"""Covid19_Prediction_main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XPPtAsuLGjbaeArEIzGFsI5i7Qlqmpjb

# **COVID19 Prediction**
"""

import os
import pickle
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.utils import plot_model
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential, Input
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from sklearn.metrics import confusion_matrix, classification_report
from covid19_prediction_module import ModelDevelopment, ModelEvaluation, Figures

"""# STEP 1) DATA LOADING"""

CSV_PATH_TRAIN = os.path.join(os.getcwd(),'cases_malaysia_train.csv')
df_train = pd.read_csv(CSV_PATH_TRAIN, na_values = [' ','?'])

CSV_PATH_TEST = os.path.join(os.getcwd(),'cases_malaysia_test.csv')
df_test = pd.read_csv(CSV_PATH_TEST, na_values = [' ','?'])

"""# STEP 2) DATA INSPECTION"""

df_train.head()

df_test.head()

df_train.info()

df_test.info()

df_train.isna().sum()

df_test.isna().sum()

df_train.describe().T

plt.figure(figsize=(10,6))
plt.plot(df_train['cases_new'])
plt.show()

mms = MinMaxScaler()
MMS_PATH = os.path.join(os.getcwd(), 'mms.pkl')

with open(MMS_PATH, 'wb') as file:
    pickle.dump(mms, file)

"""# STEP 3) DATA CLEANING"""

df_train.interpolate(method ='linear', inplace=True)

df_test.interpolate(method ='linear', inplace=True)

"""# STEP 4) FEATURES SELECTION

Train dataset
"""

X = df_train['cases_new'] # only 1 feature

mms = MinMaxScaler()
X = mms.fit_transform(np.expand_dims(X, axis=1))

win_size = 30
X_train = []
y_train = []

for i in range(win_size, len(X)): # 30, 680
  X_train.append(X[i-win_size:i])
  y_train.append(X[i])

X_train = np.array(X_train)
y_train = np.array(y_train)

"""Test dataset"""

dataset_concat = pd.concat((df_train['cases_new'],df_test['cases_new']))

"""Method 1"""

# length_days_1 = len(dataset_concat) - len(df_test) - win_size # 780 - 100 - 30
# tot_input_1 = dataset_concat[length_days_1:]

"""Method 2"""

length_days_2 = win_size + len(df_test) # 30 + 100
tot_input_2 = dataset_concat[-length_days_2:]

Xtest = mms.transform(np.expand_dims(tot_input_2, axis=1))

X_test = []
y_test = []

for i in range(win_size, len(Xtest)):
  X_test.append(Xtest[i-win_size:i])
  y_test.append(Xtest[i])

X_test = np.array(X_test)
y_test = np.array(y_test)

"""# STEP 5) DATA PREPROCESSING

MODEL DEVELOPMENT
"""

input_shape = np.shape(X_train)[1:]
nb_class = len(np.unique(y_train, axis=0))

md = ModelDevelopment()
model = md.sequential_model(input_shape,nb_class=1,
                    nb_node=64, dropout_rate=0.1)

plot_model(model, show_shapes=True, show_layer_names=True)

"""MODEL COMPILATION"""

model.compile(optimizer='adam',loss='mse',
              metrics=['mean_absolute_percentage_error','mse'])

"""Callbacks"""

LOGS_PATH = os.path.join(os.getcwd(),'logs',datetime.datetime.now().
                         strftime('%Y%m%d-%H%M%S'))

tensorboard_callback = TensorBoard(log_dir=LOGS_PATH,histogram_freq=1)

!zip -r /content/logs.zip /content/logs
from google.colab import files
files.download("/content/logs.zip")

"""MODEL TRAINING"""

hist = model.fit(X_train, y_train, epochs = 300,
                 validation_data = (X_test, y_test),
                 callbacks = tensorboard_callback)

"""Load the TensorBoard notebook extension"""

# Commented out IPython magic to ensure Python compatibility.
# %load_ext tensorboard

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs

"""To show available keys"""

hist.history.keys()

"""MODEL EVALUATION"""

predicted_new_cases = model.predict(X_test)

me = ModelEvaluation()
plot_hist = me.plot_hist_graph(hist,mse=2,valmse=5)

actual_cases = mms.inverse_transform(y_test)
predicted_cases = mms.inverse_transform(predicted_new_cases)

fg = Figures()
plot_fig = fg.plot_fig(y_test,predicted_new_cases)

"""Check MAPE"""

mape = mean_absolute_percentage_error(actual_cases, predicted_cases)
print('Mean Absolute Percentage Error:', mape)