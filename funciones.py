import cv2
import random
import numpy as np
def CARGAR_IMAGEN():
    img = cv2.imread('galeria/persona.jpg',-1) # Segundo argumento modifica la tonalidad 0=escalas de grises -1=normal
    img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
    return img

def ABRIR_CAMARA(camara):
    cap = cv2.VideoCapture(camara) #DEFINIMOS LA CAMARA
    
    while True:
        ret, frame = cap.read()
        cv2.imshow('IG: manuel_rc12', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyWindow()






