import cv2
import funciones


img=funciones.imagen()
img = cv2.imshow('IG: manuel_rc12',img)
cv2.waitKey(5000)
print(img)