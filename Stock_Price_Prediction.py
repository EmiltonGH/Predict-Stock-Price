import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt


data = yf.download('AAPL', start = '2015-01-01', end = '2023-01-01')
print(data.head())

data['Target'] = data['Close'].shift(-1)
data.dropna(inplace = True)

X = data[['Close']]
y = data['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = False)

model = RandomForestRegressor(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

MAE = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {MAE}")

plt.figure(figsize = (10,6))
plt.plot(y_test.values, label = "Actual Price", color = 'blue')
plt.plot(y_pred, label = "Predicted Price", color = 'red')
plt.title('Stock Price Prediction')
plt.xlabel('Stock Price')
plt.legend()
plt.show()