# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('01_homeprices.csv')

x= dataset.iloc[:, :-1].values
y= dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train.reshape(-1, 1))
y_test = y_test.reshape(-1, 1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


from sklearn.linear_model import LinearRegression

# Create the regression model
regressor = LinearRegression()

# Fit the model with the training data
regressor.fit(X_train, y_train)


# Area values for prediction (in square feet)
areas = np.array([[3300], [5000]])

# Scale the areas using the same scaler as for the training data
areas_scaled = sc_X.transform(areas)

# Predict the prices using the trained model
price_pred_scaled = regressor.predict(areas_scaled)

# Inverse scale the predicted prices
price_pred = sc_y.inverse_transform(price_pred_scaled)

# Output the predicted prices
print("Predicted price for 3300 sq ft:", price_pred[0])
print("Predicted price for 5000 sq ft:", price_pred[1])
