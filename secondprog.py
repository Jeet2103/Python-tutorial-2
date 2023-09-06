import cv2 as cv
img = cv.imread("WIN_20221105_21_12_17_Pro.jpg")
cv.imshow('Jeet',img)
B,G,R = cv.split(img)
cv.imshow('Blue',B)
cv.imshow('green',G)
cv.imshow('red',R)
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',img_hsv)
H,S,V = cv.split(img_hsv)
cv.imshow('hue',H)
cv.imshow('saturation',S)
cv.imshow('value',V)
cv.cvtColor
cv.waitKey(0)
cv.destroyAllWindows()