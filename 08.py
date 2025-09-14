import cv2

img = cv2.imread("demon.jpg")

gauss = cv2.GaussianBlur(img, (7,7), 0)
median = cv2.medianBlur(img, 7)

cv2.imshow("origianl", img)
cv2.imshow("Gaussian", gauss)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyAllWindows