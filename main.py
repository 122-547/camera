import cv2

cam = cv2.VideoCapture(0)

for i in range(30):
       cam.read()

ret, frame = cam.read()
cv2.imwrite('cam.png', frame)
cam.release()