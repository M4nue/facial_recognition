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

def ABRIR_CAMARA_FILTRO(camara):
    cap = cv2.VideoCapture(camara) #DEFINIMOS LA CAMARA
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        eight = int(cap.get(4))
        
        hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #FILTRO HVS

        color_hsv_claro = np.array([0, 1, 1])   
        color_hsv_oscuro = np.array([30, 255, 255])#ESTOS VALORES DEBEN SER AJUSTADOS A TU ENTORNO EN FORMATO HSV
 
        mascara = cv2.inRange(hvs,color_hsv_claro,color_hsv_oscuro) #CREACION DE MASCARA SOBRE EL FILTRO

        resultado_img_mascara = cv2.bitwise_and(frame, frame, mask=mascara)

        cv2.imshow('IG: manuel_rc12', resultado_img_mascara)
        if cv2.waitKey(1) == ord('q'):
            break








