import cv2

img=cv2.imread('1.jpg',0)
c = float(input("Enter The constant value :"))
img1=img*c
cv2.imshow('image',img1)
cv2.imshow('image org',img)
cv2.waitKey(0)
cv2.destroyAllWindows()