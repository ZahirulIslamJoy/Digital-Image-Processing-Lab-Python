import cv2
import matplotlib.pyplot as plt

image=plt.imread("../image/image.jpg")
grayscale=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
resizeImage=cv2.resize(grayscale,(512,512))
plt.imshow(resizeImage,cmap="gray")
while(resizeImage.shape[0]>=1 and resizeImage.shape[1]>=1):
        plt.subplot(2,2,3)   
        plt.imshow(resizeImage,cmap="gray")
        plt.pause(1)
        resizeImage=cv2.resize(resizeImage,(resizeImage.shape[0]//2,resizeImage.shape[1]//2))
        
plt.show()