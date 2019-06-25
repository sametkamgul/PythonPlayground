import cv2 as cv
import numpy as np
import sys

faceCascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
smileCascade = cv.CascadeClassifier('haarcascades/haarcascade_smile.xml')
cap = cv.VideoCapture(0)
sF = 1.05

while True:
	ret, frame = cap.read() # Capture frame-by-frame
	img = frame
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor= sF,
		minNeighbors=8,
		minSize=(55, 55),
		flags = cv.CASCADE_SCALE_IMAGE)
		# ---- Draw a rectangle around the faces

	for (x, y, w, h) in faces:
		cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		smile = smileCascade.detectMultiScale(
				roi_gray,
				scaleFactor= 1.7,
				minNeighbors=22,
				minSize=(25, 25),
				flags = cv.CASCADE_SCALE_IMAGE
				)

		# Set region of interest for smiles
		for (x, y, w, h) in smile:
			print("Found", len(smile), "smiles!")
			cv.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
			#print "!!!!!!!!!!!!!!!!!"
		if cv.waitKey(33) == ord('a'):
			break
		cv.imshow('Smile Detector', frame)
cap.release()
cv.destroyAllWindows()

