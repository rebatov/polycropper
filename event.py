import cv2
import numpy as np

def on_mouse(event, x, y, flags,(cPts,overlayImage,resetImage)):
    if event==cv2.EVENT_LBUTTONUP:
        cPts[0].append([x,y])
        cv2.circle(overlayImage,(x,y),5,(255),-1)
    elif event==cv2.EVENT_RBUTTONUP:
        cPts[0]=[]
        print cPts
        overlayImage[:]=resetImage[:]


cvImage=cv2.imread('test.jpg')
grayscaleImage=cv2.cvtColor(cvImage, cv2.COLOR_BGR2GRAY)
overlayImage=np.copy(grayscaleImage)
tmpImage = np.copy(cvImage)
cv2.namedWindow('Eventwindow')
cPts=[[]]
cv2.setMouseCallback('Eventwindow',on_mouse,(cPts,cvImage,tmpImage))
opacity=0.4
while True:
    displayImage=cv2.addWeighted(cvImage,opacity,tmpImage,1-opacity,0)
    cv2.imshow('Eventwindow',displayImage)
    keyPressed=cv2.waitKey(1) & 0xFF
    if keyPressed==ord("q"):
        break
    elif keyPressed==ord("s"):
        print cPts
        cv2.drawContours(cvImage,np.array(cPts),0,0)
        cv2.imshow('overlay',cvImage)
        roi_corners = np.array(cPts,dtype=np.int32)
        mask = np.zeros(cvImage.shape, dtype=np.uint8)
        channel_count = cvImage.shape[2]
        ignore_mask_color = (255,)*channel_count
        print ignore_mask_color
        # maskImage=np.zeros_like(grayscaleImage)
        cv2.fillPoly(mask, roi_corners, ignore_mask_color)
        cv2.imshow('mask',mask)
        masked_image = cv2.bitwise_and(tmpImage, mask)
        new_image = cv2.bitwise_not(masked_image)
        cv2.imshow('masked',masked_image)
        cv2.imshow('new',new_image)
        # cv2.imshow('mask',maskImage)
        # cv2.drawContours(maskImage,np.array(cPts),0,255,-1)
        # extractedImage=np.bitwise_and(grayscaleImage,maskImage)
        # cv2.imshow('extractedImage',extractedImage)
cv2.destroyAllWindows()
