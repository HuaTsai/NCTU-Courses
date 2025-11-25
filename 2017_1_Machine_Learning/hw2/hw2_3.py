import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def hw2_3_1():
  global X, T, N, D, X_test, T_test, N_test
  W = np.zeros((N,D))
  Softmax = np.zeros((N,1))
  for i in range(N):
    
  np.mat(W).T * 
  Ew = - T * Y
  


#def hw2_3_2():


#def hw2_3_3():


#def hw2_3_4():


#def hw2_3_5():


#def hw2_3_6():


def main():
  global X, T, X_test, T_test, D
  print("Machine Learning Homework #3")
  print("Please type hw2_3_x() to see my homework output")
  print("Substitute x to 1, 2, 3, 4, 5, or 6")
  fin = pd.read_csv("train.csv").as_matrix()
  X = fin[:, 4:]
  T = fin[:, 1:4]
  N = X.shape[0]
  D = X.shape[1]
  fin2 = pd.read_csv("test.csv").as_matrix()
  X_test = fin2[:, 3:]
  T_test = fin2[:, 0:3]
  N_test = X_test.shape[0]

if __name__ == '__main__':
  main()
