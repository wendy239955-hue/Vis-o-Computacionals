import cv2

img = cv2.imread("demon.jpg")

#rotacao 90
rot90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#rotacao 45 em tornodo centro
(h,w) = img.shape[:2]
centro = (w//2, h//2)
matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)
rot45 = cv2.warpAffine(img, matriz, (w, h))

cv2.imshow("origial", img)
cv2.imshow("90 graus", rot90)
cv2.imshow("45 graus0", rot45)
cv2.waitKey(0)
cv2.destroyAllWindows()
