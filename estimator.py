import numpy as np

# Data
X_A = np.array([[1.0, 2.2, 2.0, 1.5, 3.2]])
X_B = np.array([[1.3, 1.1, 2.4, 3.2, 1.2]])
W_A = np.arange(start=0.0, stop=10.1, step=1)/10    # Like this to avoid the 2.000000002 error
W_B = np.arange(start=20.0, stop=30.1, step=1)/10
Pr = np.array([[0, 1, 1, 0, 1]])

def estimator(X, Y, W_X, W_Y):
    """
        X, Y are arrays of random variables.
        W_X, W_Y are arrays of weights.
        We calculate the matrix with the values of M_w for each pair of variables and weights.
    """
    return (Pr.T*np.ones((1,len(W_X)))-1/(1+np.e**(-X.T*W_X-Y.T*W_Y)))**2

def mse(M):
    return np.ones((1, (M.shape[0]))).dot(M)    # Change the matrix to 1xlen... to calculate the sums of each column.
    
def test():
    matrix = mse(estimator(X_A, X_B, W_A, W_B))/len(W_A)
    for i in range(len(W_A)):
        print(f"The MSE for W_A = {W_A[i]}, W_B = {W_B[i]} is equal to {matrix[0][i]}")
    return
test()
