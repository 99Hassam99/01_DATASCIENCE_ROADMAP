import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import math

def predict_using_sklearn(x,y):
    r = LinearRegression()
    r.fit(x.reshape(-1, 1), y)  # Reshape x for sklearn
    return r.coef_, r.intercept_

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.01
    cost_previous = float('inf')

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        if math.isclose(cost, cost_previous, rel_tol=1e-6):
            break
        cost_previous = cost

        print("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost,i))

    return m_curr,b_curr

if __name__ == "__main__":
    df = pd.read_csv('03_test_scores.csv')
    x = np.array(df.math)
    y = np.array(df.cs)

    # Standardize the input data (x)
    scaler = StandardScaler()
    x_standardized = scaler.fit_transform(x.reshape(-1, 1)).flatten()

    m,b = gradient_descent(x_standardized,y)
    print('Using gradient descent function: Coef {} intercept {}'.format(m,b))

    m_sklearn, b_sklearn = predict_using_sklearn(x_standardized,y)
    print("Using sklearn: Coef {}, Intercept {}".format(m_sklearn,b_sklearn))