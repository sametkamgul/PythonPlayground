import cv2
import numpy as np



def imageOverlayF(foreGroundImage,background):
	global outImage
	# Read the foreground image with alpha channel
	foreGroundImage = cv2.resize(foreGroundImage,(1920,1080))

	# Split png foreground image
	b,g,r,a = cv2.split(foreGroundImage)

	# Save the foregroung RGB content into a single object
	foreground = cv2.merge((b,g,r))

	# Save the alpha information into a single Mat
	alpha = cv2.merge((a,a,a))

	# Read background image
	# background = cv2.imread("testImages/background.jpg")

	# Convert uint8 to float
	foreground = foreground.astype(float)
	background = background.astype(float)
	alpha = alpha.astype(float)/255

	# Perform alpha blending
	foreground = cv2.multiply(alpha, foreground)
	background = cv2.multiply(1.0 - alpha, background)
	outImage = cv2.add(foreground, background)

	# outImage = cv2.blur(outImage,(2,2))
	cv2.imwrite("outImgPy.png", outImage)



if __name__ == "__main__":
	print("App is started!")
	cap = cv2.VideoCapture(0)
	cap.set(3,1920)
	cap.set(4,1080)
	_, frame = cap.read()
	print(str(frame.shape))
	print("Photo is captured!")
	img = frame
	
	lowerBound=np.array([33,80,40])
	upperBound=np.array([102,255,255])

	kernelOpen=np.ones((1,1))
	kernelClose=np.ones((10,10))


	bgImage = cv2.imread("testImages/bg.png")
	# img = cv2.imread("testImages/pic2.jpg")
	img = cv2.resize(img,(1920,1080))
	height,width,_ = img.shape
	blankImage = np.zeros((height,width,4), np.uint8)


	#convert BGR to HSV
	imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	# create the Mask
	mask = cv2.inRange(imgHSV,lowerBound,upperBound)
	#morphology
	maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
	maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

	maskFinal=maskClose
	conts,h,w=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	print("Processing image...")
	for x in range(width):
		for y in range(height):
			if mask[y][x] == 0:
				blankImage[y][x][0] = img[y][x][0]
				blankImage[y][x][1] = img[y][x][1]
				blankImage[y][x][2] = img[y][x][2]
				blankImage[y][x][3] = 255
			else:
				blankImage[y][x][0] = 0
				blankImage[y][x][1] = 0
				blankImage[y][x][2] = 0
				blankImage[y][x][3] = 0
				


	
	# blankImage = cv2.blur(blankImage,(2,2))
	blankImage = cv2.GaussianBlur(blankImage,(3,3),3)
	imageOverlayF(blankImage,bgImage)
	# cv2.waitKey(0)
	print("Process is done!")