import cv2
import sys

body_cascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')

while True:
	ret,frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	body = body_cascade.detectMultiScale(gray,1.3,5)

	for(x,y,w,h) in body:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('Video', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
	
