import numpy as np


from scipy.optimize import minimize
from scipy.linalg import sqrtm


def trace(mat):
    """returns the trace of a matrix"""
    return sum(np.diag(mat))

def isPosDef(mat):
    """returns if a matrix is positive definite or not (bool)"""
    return all(np.linalg.eigh(mat)[0] > 0)

def funA2(x, R, n, m, A1):
    """function to minimize A_2 described by equation 8

    takes in A2 (x) as 1-d array to work with scipy.optmize.minimize
    """
    A2 = x.reshape(m-n, m)
    R12 = R[0:n, n:m]
    R22 = R[n:m, n:m]

    val = (0.5 * trace(np.matmul(np.matmul(A2, A2.T) - R22,
                                np.matmul(A2, A2.T) - R22))
          + trace(np.matmul((np.matmul(A1, A2.T)- R12).T,
                            np.matmul(A1, A2.T) - R12)))

    return val

def constraint(x, R, n, m):
    """constraint of equation 8

    takes in A2 (x) as 1-d array to work with scipy.optmize.minimize
    """
    A2 = x.reshape(m-n, m)
    R22 = R[n:m, n:m]

    return np.diag(np.matmul(A2, A2.T)) - np.diag(R22)

def makePosDef(R, n):
    """apply the Knol and Ten Berg (1989) algorithm"""
    m = R.shape[0]
    A11 = sqrtm(R[0:n, 0:n])
    A12 = np.zeros((n, m-n))
    A1 = np.concatenate((A11, A12), axis=1)

    x0 = R[n:m, 0:m].reshape((m-n)*m, )  # inital A2 guess; 1-d array
    args = (R, n, m, A1)  # additional args for funA2
    cons = ({'type': 'eq', 'fun': constraint, 'args': (R, n, m)})

    res = minimize(funA2, x0, args, constraints=cons)
    A2 = res.x.reshape(m-n, m)

    A = np.concatenate((A1, A2))
    G = np.matmul(A, A.T)

    return G
