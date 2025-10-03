import cv2
import os

#read img
img_pat =os.path.join('.','data','Professional.jpg')
img = cv2.imread(img_pat)


#visualize imgg  
cv2.imshow('image',img)
cv2.waitKey(100) 
print("the normal image size is:",img.shape)  #height,width <output size>


#resize img ----------------------------------------------------------------------------------------------
resize_img =cv2.resize(img,(400,560))    #width, height syntax of resized
# to calculate new_hgt =int((old_hgt/old_wid)*new_wid)

cv2.imshow('resized image',resize_img)
#cv2.waitKey(0)
print("the resized image size is:",resize_img.shape)


#crop img ------------------------------------------------------------------------------------------------
cropped_img = img[250:680,420:840]   # img[x-axis from:To,y-axis from:TO]
cv2.imshow('cropped img',cropped_img)   
cv2.waitKey(0)
print("the cropped image size is:",cropped_img.shape)   


