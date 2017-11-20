import cv2
import numpy as np

img = cv2.imread('map3.pgm')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,1,300,apertureSize = 3)
minLineLength = 100
maxLineGap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/180,25,minLineLength,maxLineGap)

print lines
print lines.shape



for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

#cv2.line(img,(468,63),(442,243),(0,255,0),2)
#cv2.line(img,(476,63),(443,379),(0,255,0),2)
#cv2.line(img,(212,210),(136,513),(0,255,0),2)



cv2.imwrite('lines3.jpg',img)

for x1,y1,x2,y2 in lines[0]:
    print "1",x1,y1
    print "2",x2,y2

print lines.shape
