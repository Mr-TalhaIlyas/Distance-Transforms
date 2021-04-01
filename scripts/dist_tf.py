import numpy as np
import matplotlib.pyplot as plt
import cv2

def dist_transformations(img = None, transformation_metric = 'Euclidean'):
    if img == None:
        data = np.random.rand(100,100)
        data = (data>0.9999).astype(np.uint32)
    else:
        data = img
    w, h = data.shape
    dist = np.zeros([w, h], np.uint32)
    dist[np.where(data==0)] = 1e7
    if transformation_metric=='Chess_Board':
        for i in range(1, w-1, 1):
            for j in range(1, w-1, 1):
                AL1 = dist[i, j-1]
                AL2 = dist[i-1, j-1]
                AL3 = dist[i-1, j]
                AL4 = dist[i-1, j+1]
                
                D1 = max(abs(i-(i)),   abs(j-(j-1)))
                D2 = max(abs(i-(i-1)), abs(j-(j-1)))
                D3 = max(abs(i-(i-1)), abs(j-(j)))
                D4 = max(abs(i-(i-1)), abs(j-(j+1)))
                dist[i, j] = min(dist[i, j], (D1+AL1), (D2+AL2), (D3+AL3), (D4+AL4))
                
        for i in range(w-2, 1, -1):
            for j in range(h-2, 1, -1):
                BR1 = dist[i, j+1]
                BR2 = dist[i+1, j+1]
                BR3 = dist[i+1, j]
                BR4 = dist[i+1, j-1]
                
                D1 = max(abs(i-(i)), abs(j-(j+1)))
                D2 = max(abs(i-(i+1)), abs(j-(j)))
                D3 = max(abs(i-(i+1)),     abs(j-(j+1)))
                D4 = max(abs(i-(i+1)), abs(j-(j-1)))
                dist[i, j] = min(dist[i, j], (D1+BR1), (D2+BR2), (D3+BR3), (D4+BR4))
        transformed = dist[3:w-3, 3:h-3]
    elif transformation_metric=='City_Block':
        for i in range(1, w-1, 1):
            for j in range(1, w-1, 1):
                AL1 = dist[i-1, j]
                AL2 = dist[i, j-1]
                
                D1 = (abs(i-(i-1))+  abs(j-(j)))
                D2 = (abs(i-(i))+ abs(j-(j-1)))
                
                dist[i, j] = min(dist[i, j], (D1+AL1), (D2+AL2))
                
        for i in range(w-2, 1, -1):
            for j in range(h-2, 1, -1):
                BR1 = dist[i, j+1]
                BR2 = dist[i+1, j]
                
                
                D1 = (abs(i-(i))+ abs(j-(j+1)))
                D2 = (abs(i-(i+1))+ abs(j-(j)))
                
                dist[i, j] = min(dist[i, j], (D1+BR1), (D2+BR2))
                
        transformed = dist[3:w-3, 3:h-3]
    elif transformation_metric=='Euclidean':
       dt = dist
       x = 0
       y = 0
       for x in range(1, w):
          if data[x,y] == 0:
             dt[x,y] = 3 + dt[x-1,y]
       for y in range(1, h):
          x = 0
          if data[x,y] == 0:
             dt[x,y] = min(3 + dt[x,y-1], 4 + dt[x+1,y-1])
          for x in range(1, w-1):
             if data[x,y] == 0:
                dt[x,y] = min(4 + dt[x-1,y-1], 3 + dt[x,y-1], 4 + dt[x+1,y-1], 3 + dt[x-1,y])
          x = w-1
          if data[x,y] == 0:
             dt[x,y] = min(4 + dt[x-1,y-1], 3 + dt[x,y-1], 3 + dt[x-1,y])
       # Backward pass
       for x in range(w-2, -1, -1):
          y = h-1
          if data[x,y] == 0:
             dt[x,y] = min(dt[x,y], 3 + dt[x+1,y])
       for y in range(h-2, -1, -1):
          x = w-1
          if data[x,y] == 0:
             dt[x,y] = min(dt[x,y], 3 + dt[x,y+1], 4 + dt[x-1,y+1])
          for x in range(1, w-1):
             if data[x,y] == 0:
                dt[x,y] = min(dt[x,y], 4 + dt[x+1,y+1], 3 + dt[x,y+1], 4 + dt[x-1,y+1], 3 + dt[x+1,y])
          x = 0
          if data[x,y] == 0:
             dt[x,y] = min(dt[x,y], 4 + dt[x+1,y+1], 3 + dt[x,y+1], 3 + dt[x+1,y])
             transformed = dt
             
    return transformed, img
#%%
img = cv2.imread('C:/Users/Talha/Desktop/dots2.png',0)
transformed, img = dist_transformations(img = None, transformation_metric = 'City_Block') #Metric is one of Euclidean, Chess_Board, City_Block
plt.imshow(transformed)
plt.contour(transformed, colors='k', linestyles  = '-.')
