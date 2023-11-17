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
        
        
        
    def forward(self, image_data_quantized):
    
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]//2
        print("f:", filas)
        print("c", columnas)
        
        #Hay que comprobar que la num de columnas sea un numero par, sino habra que replicar la ultima columna y añadirla a la matriz (imagen)
        if((columnas%2)!=0):
            #get ultima columna de la imagen
            #añadir columna a matriz -> sth like reshape matriz
            k=1
            

       
        
        a = 0
        b = 0
        c=0
        niveles=0
        result=image_data_quantized
        L=image_data_quantized
        H=image_data_quantized
        matriz_actual_levels=self.original_image
       
        for x in range(self.levels):           
            for z in range(matriz_actual_levels.shape[0]): #Dimension
                for i in range(matriz_actual_levels.shape[1]): #Filas (fijamos filas)
                    for j in range((matriz_actual_levels.shape[2]//2)): #Columnas (movemos por cada columna)
                        
                        a = int(matriz_actual_levels[z][i][2*j])
                        b = int(matriz_actual_levels[z][i][2*j+1])
                        op = b+int(int(a-b)/2)
                        print(op)
                        L[z][i][j] = op
                        H[z][i][j] = int(a-b)
                        result[z][i][j]=L[z][i][j]
                        result[z][i][j+matriz_actual_levels.shape[2]//2]= H[z][i][j]
            print(result)

        #Forward vertical - Trabaja solo con la banda L y nos genera la matriz LL|
        #                                                                      LH|
                        #filas      ,    cols
            LL = np.empty((matriz_actual_levels.shape[0],L.shape[1]//2,L.shape[2]))
            LH = np.empty((matriz_actual_levels.shape[0], L.shape[1]//2,L.shape[2]))
            for z in range(L.shape[0]): #Dimension
                for j in range(L.shape[2]): #Columnas (fijamos columna)
                    for i in range(L.shape[1]//2): #Filas (movemos por cada fila)
                        a_L = int(L[z][2*i][j])
                        b_L = int(L[z][2*i+1][j])
                        LL[z][i][j] = int(b_L + int(int(a_L-b_L)/2))
                        LH[z][i][j] = (a_L-b_L)
            matriz_actual_levels=LL
            niveles=niveles+1
        

            
        
        #Forward horizontal - nos genera  la matriz L|H
        
        
        
    
    
    
    
