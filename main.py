import cv2
import funciones
import numpy as np


funciones.ABRIR_CAMARA(0)

img=funciones.CARGAR_IMAGEN()
img = cv2.imshow('IG:@manuel_rc12',img)
cv2.waitKey(5000)
print(img)
