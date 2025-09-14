import cv2

img = cv2.imread("demon.jpg")

#reduz metade
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#aumenta o dobro
large = cv2.resize(img, (0,0), fx=2, fy=2)

cv2.imshow("Original", img)
cv2.imshow("Reduzida", small)
cv2.imshow("Ampliada", large)
cv2.waitKey(0)
cv2.destroyAllWindows()