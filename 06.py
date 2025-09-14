import cv2

img = cv2.imread("demon.jpg")

#selecionar regiao
roi = img[50:200, 100:300]

cv2.imshow("Original", img)
cv2.imshow("Recorte", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

