import cv2
img=cv2.imread("sparrow.jpg",1)
print (img)
cv2.imshow("bird",img)
k=cv2.waitkey(0)
if k==27:
    cv2.destroyAllWindows() 
