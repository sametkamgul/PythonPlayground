import numpy as np
import cv2 as cv

def rotateImage(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
  return result

if __name__ == '__main__':
	print('[INFO] app is started')
	angle = 45 # in degree, counter-clockwise rotation
	img = cv.imread('testImages/robot.jpg')
	output = rotateImage(img, angle)
	cv.imwrite('outputImages/rotated-image.png', output)
	print('[INFO] job is done')

