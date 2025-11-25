import numpy as np
from sklearn import preprocessing
from PIL import Image
from sklearn.metrics.pairwise import euclidean_distances

def kmeans(K):
  global data, newdata
  minvalue = np.amin(data)
  maxvalue = np.amax(data)
  mu = np.zeros((K,5))
  for i, c in enumerate(mu):
    mu[i] = np.random.uniform(minvalue, maxvalue, 5)
  for i in range(100):
    distance = np.ndarray(shape=(K))
    for index, center in enumerate(mu):
      distance[index] = euclidean_distances(data.reshape(1,-1), mu.reshape(1,-1))
    cluster[i] = np.argmin(distance)
    
    for index, item in enumerate(result):
      newdata[index][0] = int(round(mu[item][0] * 255))
      newdata[index][1] = int(round(mu[item][1] * 255))
      newdata[index][2] = int(round(mu[item][1] * 255))

def main():
  global data, newdata 
  image = Image.open("hw3_img.jpg")
  w = image.size[0]
  h = image.size[1]
  data = np.ndarray(shape=(w * h,5), dtype=float)
  newdata = np.ndarray(shape=(w * h,5), dtype=float)
  for i in range(h):
    for j in range(w):
      data[j+i*h,0] = image.getpixel((j,i))[0]
      data[j+i*h,1] = image.getpixel((j,i))[1]
      data[j+i*h,2] = image.getpixel((j,i))[2]
      data[j+i*h,3] = j
      data[j+i*h,4] = i
  data = preprocessing.normalize(data)
  for k in [2,3,5,20]
    kmeans(k)
    newimage = Image.new("RGB", (w, h))
    for x in range(w):
      for y in range(h):
        newimage.putpixel((x,y),(int(newdata[y*w+x][0]),int(newdata[y*w+x][1]),int(newdata[y*w+x][2])))
    image.save("K=" + str(k))

if __name__ == '__main__':
  main()
