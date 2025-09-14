import cv2

#carregar a imaem
img = cv2.imread("demon.jpg")

#exibir imagem em um ajenla
cv2.imshow("demon.jpg", img)

#espera ate press a tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
