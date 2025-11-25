import matplotlib.pyplot as plt
import numpy as np
import scipy.io
from scipy.stats import wishart, multivariate_normal

def main():
  global X
  fin = scipy.io.loadmat("1_data.mat")
  X = fin['r2']
  wishart(x, 1, np.eye(2))
  multivariate_normal

if __name__ == '__main__':
  main()
