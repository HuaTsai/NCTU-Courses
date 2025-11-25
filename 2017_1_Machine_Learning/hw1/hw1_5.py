import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import scipy.io


def hw1_5_1():
  print("run hw1_5_1\n")
  print("M = 1:")
  curveFit(1)
  print("w = ")
  print(w)
  print()
  printRMS()
  print("M = 2:")
  curveFit(2)
  print("w = ")
  print(w)
  print()
  printRMS()


def hw1_5_2():
  global x, x_test
  print("run hw1_5_2\n")
  xBackup = x
  x_testBackup = x_test
  trainRMS = []
  testRMS = []
  for i in range(4):
    print("(" + str(i + 1) + ") discard x" + str(i + 1) + ":\n")
    x = xBackup[:, np.delete(np.arange(4), i)]
    x_test = x_testBackup[:, np.delete(np.arange(4), i)]
    curveFit(2)
    trainRMS.append(trainErrorRMS)
    testRMS.append(testErrorRMS)
    printRMS()
  for i in range(4):
    for j in range(i + 1, 4):
      if i == 0:
        print("(" + str(i + j + 4) + ") discard x" + str(i + 1) + ", x" +
              str(j + 1) + ":\n")
      else:
        print("(" + str(i + j + 5) + ") discard x" + str(i + 1) + ", x" +
              str(j + 1) + ":\n")
      x = xBackup[:, np.delete(np.arange(4), (i, j))]
      x_test = x_testBackup[:, np.delete(np.arange(4), (i, j))]
      curveFit(2)
      trainRMS.append(trainErrorRMS)
      testRMS.append(testErrorRMS)
      printRMS()
  for i in range(4):
    print("(" + str(i + 11) + ") only x" + str(i + 1) + ":\n")
    x = np.array(np.mat(xBackup[:, i]).T)
    x_test = np.array(np.mat(x_testBackup[:, i]).T)
    curveFit(2)
    trainRMS.append(trainErrorRMS)
    testRMS.append(testErrorRMS)
    printRMS()
  print(
      "The x-axis of this figure (from 1 to 14) corresponds to the above order of discarding method\n"
  )
  print("In perspective of test data:")
  print("* 14 (only x4) has lowest RMS from 11 to 14")
  print("* 4 (discard x4) has higher RMS from 1 to 4 (means less accurate)")
  print("It it obvious that x4 plays an important role in prediction.")
  print(
      "Therefore I think x4 (petal width) is the most contributive attribute.")
  print(
      "Besides, if we ignore x1 (sepal length), then it performs the best in test data."
  )
  x = xBackup
  x_test = x_testBackup
  plt.title("RMS with discarding some data")
  plt.scatter(np.arange(1, 15), trainRMS, label='trainRMS', color='b')
  plt.plot(np.arange(1, 15), trainRMS, color='b')
  plt.scatter(np.arange(1, 15), testRMS, label='testRMS', color='r')
  plt.plot(np.arange(1, 15), testRMS, color='r')
  plt.legend()
  plt.show()


def curveFit(M):
  global w, trainErrorRMS, testErrorRMS
  initphi(M)
  w = (phi.T * phi).I * phi.T * np.mat(t).T
  tpred = np.array(phi * w).flatten()
  tpred_test = np.array(phi_test * w).flatten()
  trainError = np.sum((tpred - t)**2 / 2)
  trainErrorRMS = (2 * trainError / 120)**0.5
  testError = np.sum((tpred_test - t_test)**2 / 2)
  testErrorRMS = (2 * testError / 30)**0.5


def initphi(M):
  global phi, phi_test
  phi = np.mat(np.ones((120, 1)))
  phi = np.column_stack((phi, x))
  phi_test = np.mat(np.ones((30, 1)))
  phi_test = np.column_stack((phi_test, x_test))
  if M == 2:
    for i in range(x.shape[1]):
      for j in range(i, x.shape[1]):
        phi = np.column_stack((phi, x[:, i] * x[:, j]))
        phi_test = np.column_stack((phi_test, x_test[:, i] * x_test[:, j]))


def printRMS():
  print("trainErrorRMS: " + str(trainErrorRMS))
  print("testErrorRMS:  " + str(testErrorRMS))
  print()


def main():
  global x, t, x_test, t_test
  print("Machine Learning H mework #1")
  print("Please type hw1_5_x() to see my homework solution")
  print("Substitute x to 1 or 2")
  fin = scipy.io.loadmat("5_X.mat")
  X = fin['X']
  fin = scipy.io.loadmat("5_T.mat")
  T = fin['T'][:, 0]
  x = np.row_stack((X[0:40], X[50:90], X[100:140]))
  t = np.append(np.append(T[0:40], T[50:90]), T[100:140])
  x_test = np.row_stack((X[40:50], X[90:100], X[140:150]))
  t_test = np.append(np.append(T[40:50], T[90:100]), T[140:150])


if __name__ == '__main__':
  main()
