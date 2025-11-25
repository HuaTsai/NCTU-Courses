import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy.polynomial.polynomial as poly


def hw1_4_1():
  print("run hw1_4_1\n")
  for i in range(1, 10):
    print("M = " + str(i))
    print("w = ")
    print(allw[i - 1])
    print()
  print("trainErrorRMS: (from 1 to 9)")
  print(trainErrorRMS)
  print()
  print("testErrorRMS:  (from 1 to 9)")
  print(testErrorRMS)


def hw1_4_2():
  print("run hw1_4_2")
  print("\nOrder from 7 to 9 will cause overfitting problem")
  plt.plot(np.arange(1, 10), trainErrorRMS, c='b')
  plt.scatter(np.arange(1, 10), trainErrorRMS, c='b', label='training')
  plt.plot(np.arange(1, 10), testErrorRMS, c='r')
  plt.scatter(np.arange(1, 10), testErrorRMS, c='r', label='test')
  plt.title("hw1-4-2")
  plt.xlabel("Degree of polynomial (i.e. M)")
  plt.ylabel("Root mean square")
  plt.legend(loc='upper right')
  plt.show()


def hw1_4_3():
  trainErrorRMS_r = []
  testErrorRMS_r = []
  s = np.linspace(-20, 0, 200)
  Lambda = np.exp(s)
  phi = np.mat(np.ones((20, 1)))
  for i in range(1, 10):
    phi = np.column_stack((phi, x**i))
  for i in Lambda:
    w_r = (phi.T * phi + i * np.mat(np.identity(10))).I * phi.T * np.mat(t).T
    trainError = np.sum((poly.polyval(x, w_r) - t)**2 / 2)
    trainErrorRMS_r = np.append(trainErrorRMS_r, (2 * trainError / 20)**0.5)
    testError = np.sum((poly.polyval(x_test, w_r) - t_test)**2 / 2)
    testErrorRMS_r = np.append(testErrorRMS_r, (2 * testError / 10)**0.5)
  print("run hw1_4_3")
  plt.plot(s, trainErrorRMS_r, c='b')
  plt.scatter(s, trainErrorRMS_r, c='b', label='training')
  plt.plot(s, testErrorRMS_r, c='r')
  plt.scatter(s, testErrorRMS_r, c='r', label='test')
  plt.title("hw1-4-3")
  plt.xlabel("$\ln\lambda$")
  plt.ylabel("Root mean square")
  plt.legend(loc='upper right')
  plt.show()


def curveFit():
  global w, allw, trainErrorRMS, testErrorRMS
  allw = [0 for i in range(9)]
  trainErrorRMS = []
  testErrorRMS = []
  phi = np.mat(np.ones((20, 1)))
  for i in range(1, 10):
    phi = np.column_stack((phi, x**i))
    w = (phi.T * phi).I * phi.T * np.mat(t).T
    allw[i - 1] = np.array(w).flatten()
    trainError = np.sum((poly.polyval(x, w) - t)**2 / 2)
    trainErrorRMS = np.append(trainErrorRMS, (2 * trainError / 20)**0.5)
    testError = np.sum((poly.polyval(x_test, w) - t_test)**2 / 2)
    testErrorRMS = np.append(testErrorRMS, (2 * testError / 10)**0.5)


def curvePlot(x, y, M):
  xnew = np.linspace(x.min(), x.max(), 300)
  ynew = poly.polyval(xnew, allw[M - 1])
  plt.scatter(x, y, color='r', marker='x', label='actual data')
  plt.plot(xnew, ynew, color='b', label='fitting curve')
  plt.title("Curve")
  plt.xlabel("x")
  plt.ylabel("t")
  plt.legend(loc='upper right')
  plt.show()


def main():
  global x, t, x_test, t_test
  print("Machine Learning Homework #1")
  print("Please type hw1_4_x() to see my homework solution")
  print("Substitute x to 1, 2, or 3")
  print("--------------------------------------------------------")
  print("call function curvePlot(x, t, M) to plot fitting curve")
  print("x <- x to print training data, x_test to print test data")
  print("t <- t to print training data, t_test to print test data")
  print("x and t must be the same data source")
  print("M <- degree value from 1 to 10")
  print("e.g. curvePlot(x_test, t_test, 7)")
  fin = pd.read_csv("4_train.csv").as_matrix()
  t = fin[:, 0]
  x = fin[:, 1]
  t = t[np.argsort(x)]
  x = x[np.argsort(x)]
  fin = pd.read_csv("4_test.csv").as_matrix()
  t_test = fin[:, 0]
  x_test = fin[:, 1]
  t_test = t_test[np.argsort(x_test)]
  x_test = x_test[np.argsort(x_test)]
  curveFit()


if __name__ == '__main__':
  main()
