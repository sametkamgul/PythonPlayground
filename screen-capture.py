import pyscreenshot as ImageGrab
import cv2
import numpy as np
import time
import pyautogui

if __name__ == "__main__":
	count = 0
	native_screen_resolution = (1366, 768)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('outputImages/output-screen-capture.avi', fourcc, 24.0, native_screen_resolution)

	for x in range(120):
		screenshot = pyautogui.screenshot()
		enhanced_image = np.asarray(screenshot)
		r, g, b = cv2.split(enhanced_image)
		enhanced_image = cv2.merge([b, g, r])
		# cv2.imwrite("Output/output" + str(count) + ".png",enhanced_image)
		out.write(enhanced_image)
		print("Frame Number: " + str(count))
		count += 1
	out.release()
		