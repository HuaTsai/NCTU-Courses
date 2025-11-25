import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import math

def hw3_1_1():
  global x, t
  plt.figure('hw3-1')
  print("(th0, th1, th2, th3)    train    test")
  expkernel(1,4,0,0,1)
  expkernel(0,0,0,1,2)
  expkernel(1,4,0,5,3)
  expkernel(1,64,10,0,4)
  plt.show()

def expkernel(th0, th1, th2, th3, sub):
  global x, t, xtest, ttest
  if sub == 1:
    plt.subplot(2,2,1)
  elif sub == 2:
    plt.subplot(2,2,2)
  elif sub == 3:
    plt.subplot(2,2,3)
  else:
    plt.subplot(2,2,4)
  sample = 100
  C = np.zeros((60,60))
  for i in range(60):
    for j in range(60):
      xn = x[i]
      xm = x[j]
      C[i][j] = th0 * math.exp(-th1/2*((xn-xm) ** 2)) + th2 + th3 * xn * xm
      if i == j:
        C[i][j] = C[i][j] + 1
  C = np.mat(C)
  xx = np.linspace(0,2,sample)
  tt = np.zeros(sample)
  std = np.zeros(sample)
  k = np.zeros((60,1))
  for i in range(sample):
    for j in range(60):
      k[j] = th0 * math.exp(-th1/2*((xx[i]-x[j]) ** 2)) + th2 + th3 * xx[i] * x[j]
    tt[i] = np.mat(k).T * C.I * np.mat(t)
    std[i] = th0 + th2 + th3 * (xx[i] ** 2) - np.mat(k).T * C.I * np.mat(k)
    std[i] = math.sqrt(std[i])

  print("("+str(th0)+","+str(th1)+","+str(th2)+","+str(th3)+")   ", end="")
  tpre = np.zeros((60,1))
  k = np.zeros((60,1))
  # train data
  for i in range(60):
    for j in range(60):
      k[j] = th0 * math.exp(-th1/2*((x[i]-x[j]) ** 2)) + th2 + th3 * x[i] * x[j]
    tpre[i] = np.mat(k).T * C.I * np.mat(t)
  print(math.sqrt(np.sum((tpre - t) ** 2) / 60), end="")
  print("    ", end="")

  tpre = np.zeros((40,1))
  k = np.zeros((60,1))
  # test data
  for i in range(40):
    for j in range(60):
      k[j] = th0 * math.exp(-th1/2*((xtest[i]-x[j]) ** 2)) + th2 + th3 * xtest[i] * x[j]
    tpre[i] = np.mat(k).T * C.I * np.mat(t)
  print(math.sqrt(np.sum((tpre - ttest) ** 2) / 40))
    
  plt.scatter(x, t, color='b', marker='o', label='training data', facecolor='none')
  plt.plot(xx, tt, color='r', label='predictive distribution')
  plt.fill_between(xx, tt + std, tt - std, facecolor='pink', label='standard deviation')
  plt.title("["+str(th0)+","+str(th1)+","+str(th2)+","+str(th3)+"]")
  plt.xlabel("x")
  plt.ylabel("t")
  plt.legend(loc='upper right')
  plt.xlim((0,2))
  plt.ylim((-10,15))

def main():
  global fin, x, t, xtest, ttest
  print("Machine Learning Homework #3")
  print("Please type hw3_1_x() to see my homework output")
  print("Substitute x to 1, 2 or 3")
  fin = scipy.io.loadmat("2_data.mat")
  x = fin['x'][0:60]
  t = fin['t'][0:60]
  xtest = fin['x'][60:100]
  ttest = fin['t'][60:100]

if __name__ == '__main__':
  main()
