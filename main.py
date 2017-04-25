import cv2
import numpy as np
image = cv2.imread('test.jpg',-1)
mask = np.zeros(image.shape,dtype=np.uint8)
roi_corners = np.array([[(100,100), (300,300), (10,300), (50,600)]], dtype=np.int32)
channel_count = image.shape[2]
ignore_mask_color = (255,)*channel_count
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
masked_image = cv2.bitwise_and(image, mask)
cv2.imwrite('image_masked.png', masked_image)
tmp = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(masked_image)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("transparent.png", dst)
