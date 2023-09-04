import cv2
import matplotlib.pyplot as plt
import numpy as np

image=cv2.imread("../image/dog.jpeg",cv2.IMREAD_GRAYSCALE)
image=cv2.resize(image,(512,512))

histrogram=[0]*256

for row in image:
    for pixel_value in row:
        histrogram[int(pixel_value)] +=1
        
plt.subplot(2,2,1)
plt.bar(range(256), histrogram)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Image Histogram')

threshold = 128
thresholdImage=(image>=threshold).astype(int)
print(thresholdImage)

plt.subplot(2, 2, 2)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 3)
plt.imshow(thresholdImage, cmap='gray')
plt.title('Threashhold Image')


# Convert thresholdImage back to a NumPy array
histogram1 = [0] * 256

for row in thresholdImage:
    for pixel_value in row:
        histogram1[int(pixel_value)] += 1


print(histogram1)
plt.subplot(2, 2, 4)
plt.bar(range(256), histogram1)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('After Threshold Image Histogram')
plt.show()