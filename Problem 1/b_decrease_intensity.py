import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("../image/dog.jpeg",cv2.IMREAD_GRAYSCALE)
image=cv2.resize(image,(512,512))

numOfBits=8
# quantizedImage=[]

while numOfBits >=1:
    quantizedValue=255/(2*numOfBits-1)
    quantizedImage=(image/quantizedValue).astype(np.uint)*quantizedValue
    # plt.subplot(2,2,1)   
    plt.imshow(quantizedImage,cmap="gray")
    title = f"{numOfBits} bits"
    plt.title(title)
    plt.pause(1)
    numOfBits-=1

plt.show()