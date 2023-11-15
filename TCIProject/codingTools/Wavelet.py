import sys
import os
import numpy as np
import math

class Wavelet:
    
    
    def __init__(self,image,levels):
        self.original_image=image
        self.levels=levels
        
        self.original_image_components = image.shape[0]
        self.original_image_rows = image.shape[1]
        self.original_image_columns = image.shape[2]
        
        
        
    def forward(self):
    
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]//2
        print("f:", filas)
        print("c", columnas)
        
        #Hay que comprobar que la num de columnas sea un numero par, sino habra que replicar la ultima columna y añadirla a la matriz (imagen)
        if((columnas%2)!=0):
            #get ultima columna de la imagen
            #añadir columna a matriz -> sth like reshape matriz
            
            

        L = np.empty((filas,columnas))
        H = np.empty((filas,columnas))
        
        a = 0
        b = 0
        
        
        
        #Forward horizontal - nos genera  la matriz L|H
        for z in range(self.original_image.shape[0]): #Dimension
            for i in range(self.original_image.shape[1]): #Filas (fijamos filas)
                for j in range((self.original_image.shape[2]//2)): #Columnas (movemos por cada columna)
                    a = int(self.original_image[z][i][2*j])
                    b = int(self.original_image[z][i][2*j+1])
                    op = b+int(int(a-b)/2)
               
                    L[i][j] = op
                    H[i][j] = (a-b)
                            
        #Forward vertical - Trabaja solo con la banda L y nos genera la matriz LL|H
        #                                                                      LH|H
                        #filas      ,    cols
        Lv = np.empty((L.shape[0]//2,L.shape[1]))
        Hv = np.empty((L.shape[0]//2,L.shape[1]))

        for j in range(L.shape[1]): #Columnas (fijamos columna)
            for i in range(L.shape[0]//2): #Filas (movemos por cada fila)
                a_L = int(L[2*i][j])
                b_L = int(L[2*i+1][j])
                a_H = int(H[2*i][j])
                b_H = int(H[2*i+1][j])
                Lv[i][j] = int(b_L + int(int(a_L-b_L)/2))
                Hv[i][j] = (a_H-b_H)
                    
        print('Matriz L horizontal: \n',L) #matriz L - OK (values checked)
        print('Matriz H horizontal: \n',H) #matriz H - OK (values checked)
        print('Matriz Lv vertical: \n',Lv) #matriz LL - OK (values checked)
        print('Matriz Hv vertical: \n',Hv) #matriz LH - OK (values checked)
        
    
    
    
    

