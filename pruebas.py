import cv2
import numpy as np

cap = cv2.VideoCapture(0)
'''
#BUCLE INFINITO QUE MANTIENE LA CAMARA ABIERTA
while True:
    ret, frame = cap.read()
    cv2.imshow('IG:@manuel_rc12',frame)
    if cv2.waitKey(1) == ord('q'): #SALIDA DE BUCLE EN CASO DE PULSAR LA LETRA q
        break
cap.release() #LIBERACION DEL RECURSO "CAMARA"
cv2.destroyAllWindows() #LIMPIEZA DE TODAS LAS VENTANAS
'''
'''
#BUCLE INFINITO QUE MANTIENE LA CAMARA ABIERTA
while True:
    ret, frame = cap.read() #VARIABLES QUE CONTIENEN LAS CAPTURAS DE LA CAMARA
    
    width = int(cap.get(3)) 
    height = int(cap.get(4)) #OBTENEMOS ANCHO Y ALTO DE LA CAMARA

    imagen = np.zeros(frame.shape, np.uint8) #VARIABLE QUE SOLAPA A FRAME PARA VOLVER LA CAMARA UN "LIENZO NEGRO"
    small_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) #REESCALADO DEL FRAME
    cv2.imshow('IG:@manuel_rc12',small_frame)
    if cv2.waitKey(1) == ord('q'): #SALIDA DE BUCLE EN CASO DE PULSAR LA LETRA 1
        break
cap.release() #LIBERACION DEL RECURSO "CAMARA"
cv2.destroyAllWindows() #LIMPIEZA DE TODAS LAS VENTANAS

'''

def ABRIR_CAMARA(camara):
    cap = cv2.VideoCapture(camara) #DEFINIMOS LA CAMARA
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        eight = int(cap.get(4))
        
        hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #FILTRO DIFERENCIAR COLORES

        color_hsv_claro = np.array([0, 1, 1])   # Valores típicos inferiores para piel en HSV
        color_hsv_oscuro = np.array([30, 255, 255])  # Ajusta estos valores según tus necesidades
 
        mascara = cv2.inRange(hvs,color_hsv_claro,color_hsv_oscuro)#DETECCION DE COLORES EN X RANGO

        resultado_img_mascara = cv2.bitwise_and(frame, frame, mask=mascara)

        cv2.imshow('IG: manuel_rc12', resultado_img_mascara)
        if cv2.waitKey(1) == ord('q'):
            break

ABRIR_CAMARA(0)






