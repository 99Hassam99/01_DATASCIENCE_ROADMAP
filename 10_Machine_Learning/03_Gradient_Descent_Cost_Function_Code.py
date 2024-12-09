# The problem we are solving here is we have a value of x and y vectors, and we want to derive the best fit line
# or an equation using m and b, so we have x and y and we want to come up with a correct value of m and b and that is
# our objective.

import numpy as np

def gradient_descent(x, y):
    m_curr = b_curr = 0 # starting with some value of m & b

    # then taking baby steps to reach global minima

    iterations = 10000 # defining number of iteration like how many baby step to take

    n = len(x) # n is the length of these data points

    learning_rate = 0.08

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2 / n) * sum(x * (y - y_predicted))   # m & b partial derivatives
        bd = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))

x = np.array([1, 2, 3, 4, 5]) # using numpy array instead of simple python list as matrix multiplication is easy in numpy
y = np.array([5, 7, 9, 11, 13]) # numpy array are tends to be faster than simple python list

gradient_descent(x,y)


# Expected value of m was 2 and b was 3 and cost function value was 1 and that is the way how we can approach
# the gradient descent algorithm and stop whenever you reach some threshold of cost, or even we can compare
# cost between the different iteration, and we can find out, as the property of this curvature is that once you reach
# the global minima your cost will stay the same if you are using the correct learning rate, so here we see in our code
# that in all these iterations our cost is almost remains constant, so we can use the floating point comparison and
# compare to cost and stop whenever our cost is not reducing too much.