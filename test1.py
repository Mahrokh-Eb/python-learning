import numpy as np
import cvxopt
import cvxopt.solvers
import pandas as pd


# Reads the data from CSV files, converts it into Dataframe and returns x and y dataframes
def getDataframe(filePath):
    dataframe = pd.read_csv(filePath)
    y = dataframe['y']
    x = dataframe.drop('y', axis=1)
    y = y * 2 - 1.0

    return x, y


def compute_accuracy(predicted_y, y):
    acc = 100.0
    ########## Please Fill Missing Lines Here ##########
    return acc


def linear_kernel_point(x1, x2):
    ########## Please Fill Missing Lines Here ##########
def linear_kernel(X):
 ########## Please Fill Missing Lines Here ##########


class SVM(object):

    def __init__(self, kernel=linear_kernel, C=None):
        self.kernel = kernel
        self.kernel_point = linear_kernel_point
        self.C = C
        if self.C is not None: self.C = float(self.C)

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Kernel matrix
        K = self.kernel(X)

        # dealing with dual form quadratic optimization
        P = cvxopt.matrix(np.outer(y, y) * K)
        q = cvxopt.matrix(np.ones(n_samples) * -1)
        A = cvxopt.matrix(y, (1, n_samples), 'd')
        b = cvxopt.matrix(0.0)

        if self.C is None:
            G = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
            h = cvxopt.matrix(np.zeros(n_samples))
        else:
            tmp1 = np.diag(np.ones(n_samples) * -1)
            tmp2 = np.identity(n_samples)
            G = cvxopt.matrix(np.vstack((tmp1, tmp2)))
            tmp1 = np.zeros(n_samples)
            tmp2 = np.ones(n_samples) * self.C
            h = cvxopt.matrix(np.hstack((tmp1, tmp2)))

        # solve QP problem
        solution = cvxopt.solvers.qp(P, q, G, h, A, b)

        # Lagrange multipliers
        a = np.ravel(solution['x'])

        # Support vectors have non zero lagrange multipliers
        sv = a > 1e-5
        ind = np.arange(len(a))[sv]
        self.a = a[sv]
        self.sv = X[sv].values
        self.sv_y = y[sv].values

        print("%d support vectors out of %d points" % (len(self.a), n_samples))

        # Intercept via average calculating b over support vectors
        self.b = 0
        for n in range(len(self.a)):
            self.b += self.sv_y[n]
            self.b -= np.sum(self.a * self.sv_y * K[ind[n], sv])
        self.b /= len(self.a)

        # Weight vector
        self.w = np.zeros(n_features)
        for n in range(len(self.a)):
            self.w += self.a[n] * self.sv_y[n] * self.sv[n]

    # predict labels for test dataset
    def project(self, X):
        predict_y = np.zeros(len(X))
        ########## Please Fill Missing Lines Here ##########
        return predict_y


    def predict(self, X):
        return np.sign(self.project(X))


if __name__ == "__main__":
    # load data
    train_x, train_y = getDataframe('Data/train.csv')
    test_x, test_y = getDataframe('Data/test.csv')

    # training
    C = 500

    mysvm = SVM()

    mysvm.fit(train_x, train_y)

    # testing
    predict_y = mysvm.predict(test_x)
    n = test_x.shape[0]
    output = np.zeros((n, 2))

    output[:, 0] = test_y
    output[:, 1] = predict_y
    np.savetxt('output/test.txt', output, delimiter='\t', newline='\n')
    test_accuracy = compute_accuracy(predict_y, test_y)

    print('Test accuracy: ', test_accuracy)
