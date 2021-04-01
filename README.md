# Distance Transformations:
A distance transform, also known as distance map or distance field, is a derived representation of a digital image. In distance transformation we  label each pixel of the image with the distance to the nearest obstacle pixel. E.g.
One way to think about the distance transform is to first imagine that foreground regions in the input binary image are made of some uniform slow burning inflammable material. Then consider simultaneously starting a fire at all points on the boundary of a foreground region and letting the fire burn its way into the interior. If we then label each point in the interior with the amount of time that the fire took to first reach that point, then we have effectively computed the distance transform of that region. Figure 1 shows a distance transform for a simple rectangular shape.

img1.gif

### Distance Transforms are of following types:
•	Euclidean distance
•	City Block or Manhattan distance.
•	Chessboard distance

img2.png

### Implementation Details:
•	I used Python Language for implementing the distance transformations.
•	The filters I used for above transformations are as follows:

img4.png

## Results

img 3 5 6 7