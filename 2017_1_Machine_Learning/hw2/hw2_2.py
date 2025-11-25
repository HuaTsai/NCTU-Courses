import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import math

def hw2_2_1():
  global t, Phi, tt
  for i in [10, 15, 30, 80, 100]:
    tt = np.mat(t[:i])
    Phi = np.mat(genphi(i))
    S0inv = np.mat(10 ** (-6) * np.eye(7))
    Sn = (S0inv + Phi.T * Phi).I
    Mn = Sn * Phi.T * tt
    print("\nFor N = " + str(i) + ":")
    print("\nmean vector m:")
    print(Mn)
    print("\ncovariance matrix S:")
    print(Sn)

#def hw2_2_2():

#def hw2_2_3():

def genphi(n):
  global x
  phi = np.zeros((n,1))
  for i in range(7):
    for j in range(n):
      a = (x[j] - 2 * i / 7 ) / 0.1
      phi[j] = 1 / (1 + math.exp(-a))
    if (i == 0):
      Phi = phi
    else:
      Phi = np.column_stack((Phi, phi))
  return Phi

def main():
  global x, t, phi
  print("Machine Learning Homework #2")
  print("Please type hw2_2_x() to see my homework output")
  print("Substitute x to 1, 2 or 3")
  fin = scipy.io.loadmat("2_data.mat")
  x = fin['x']
  t = fin['t']

if __name__ == '__main__':
  main()
