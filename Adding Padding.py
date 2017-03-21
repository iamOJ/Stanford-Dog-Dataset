import cv2

BLUE=[255,0,0]

img = cv2.imread('qwerty1.jpg')
shape=img.shape
ysize=shape[0]
xsize=shape[1]
ypad=512-ysize
xpad=512-xsize
constant = cv2.copyMakeBorder(img,0,xpad,0,ypad,cv2.BORDER_CONSTANT,value=BLUE)
cv2.imwrite('qwerty2.jpg',constant)