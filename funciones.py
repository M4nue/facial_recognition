import cv2
import random
def imagen():
    img = cv2.imread('galeria/persona.jpg',-1) # Segundo argumento modifica la tonalidad 0=escalas de grises -1=normal
    img = cv2.resize(img,(0,0),fx=0.7,fy=0.7)
    return img


