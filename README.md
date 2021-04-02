[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<img alt="NumPy" src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />

# Distance Transformations:
A distance transform, also known as distance map or distance field, is a derived representation of a digital image. In distance transformation we  label each pixel of the image with the distance to the nearest obstacle pixel. E.g.
One way to think about the distance transform is to first imagine that foreground regions in the input binary image are made of some uniform slow burning inflammable material. Then consider simultaneously starting a fire at all points on the boundary of a foreground region and letting the fire burn its way into the interior. If we then label each point in the interior with the amount of time that the fire took to first reach that point, then we have effectively computed the distance transform of that region. Figure 1 shows a distance transform for a simple rectangular shape.

![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img1.gif)

### Distance Transforms are of following types:
* Euclidean distance
* City Block or Manhattan distance.
* Chessboard distance

![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img2.png)

### Implementation Details:
* I used Python Language for implementing the distance transformations.
* The filters I used for above transformations are as follows:

### Usage
If image is `None` a random grayscale image will be generated with some random points as `ones` and rest will be all `zeros`.
```python
img = cv2.imread('C:/Users/Talha/Desktop/dots2.png',0)
# Metric is one of Euclidean, Chess_Board or City_Block
transformed, img = dist_transformations(img = None, transformation_metric = 'City_Block') 
plt.imshow(transformed)
# to display contours
plt.contour(transformed, colors='k', linestyles  = '-.')
```
![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img4.png)

## Results
![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img3.png)
![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img5.png)
![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img6.png)
![alt text](https://github.com/Mr-TalhaIlyas/Distance-Transforms/blob/master/screens/img7.png)
