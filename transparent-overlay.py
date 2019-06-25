import cv2
import numpy as np

try:
	frame = cv2.imread("testImages/scene.jpg")
except:
	print("Image is not found!")
try:
	overlay = cv2.imread("testImages/overlay.png",-1)
except:
	print("Overlay Image is not found!!!")

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

	cv2.imwrite("outputImages/output-image.png", outImage)

if __name__ == "__main__":
	imageOverlayF(overlay, frame)
