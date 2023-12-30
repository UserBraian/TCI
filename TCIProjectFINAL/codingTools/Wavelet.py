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
        
        
        
    def forward(self,image_data_empty):
        
        result = image_data_empty
        print(result.shape)
        matriz_nivel_actual = np.copy(self.original_image)
        
        #Hay que comprobar que la num de columnas sea un numero par, sino habra que replicar la ultima columna y añadirla a la matriz (imagen)
        #if((m%2)!=0):
        #    kk=1
            #get ultima columna de la imagen
            #añadir columna a matriz -> sth like reshape matriz
            
        
        a = 0
        b = 0
        #print('matriz actual: \n',matriz_nivel_actual)
        
        for level in range(self.levels):
            dimension = matriz_nivel_actual.shape[0]
            filas = matriz_nivel_actual.shape[1]//(2**level)
            columnas = matriz_nivel_actual.shape[2]//(2**level)
            print('dim:', dimension)
            print("fil:", filas)
            print("col", columnas)
            
            
            #Forward horizontal - nos genera  la matriz L|H
            for dim in range(dimension): #Dimension
                for fila in range(filas): #Filas (fijamos filas)
                    for col in range(columnas//2): #Columnas (movemos por cada columna)
                        a = int(matriz_nivel_actual[dim][fila][2*col])
                        b = int(matriz_nivel_actual[dim][fila][2*col+1])
                        
                        op1 = b+int(int(a-b)/2)
                        #print('b+ a-b/2 -> op1:',op1)
                        op2=int(a-b)
                        #print('a-b -> op2:',op2)
                        
                        #banda L:
                        result[dim][fila][col]=op1
                        
                        #banda H:
                        result[dim][fila][col+columnas//2]=op2
                        
            #print('result horizontal: \n',result) #Valores correctos (checked)  result ahora es la matriz : L|H
            
            matriz_nivel_actual = np.copy(result)
            
                
            #Forward vertical - Trabaja solo con la banda L y nos genera la matriz LL|H
            #                                                                      LH|H
            for dim in range(dimension):
                for col in range(columnas//2): #Columnas (fijamos columna)
                    for fila in range(filas//2): #Filas (movemos por cada fila)
                        a_L = int(matriz_nivel_actual[dim][2*fila][col])
                        b_L = int(matriz_nivel_actual[dim][2*fila+1][col])
                        
                        op1 = b_L+int(int(a_L-b_L)/2)
                        
                        op2 = int(a_L-b_L)
                
                        #banda LL:
                        result[dim][fila][col] = b_L+int(int(a_L-b_L)/2)
                        
                        #banda LH:
                        result[dim][fila+filas//2][col] = int(a_L-b_L)
            
                
                        
            #print('result vertical: \n',result) #Valores correctos (checked) result ahora es la matriz : LL|H
            #                                                                                            LH|H
            
            matriz_nivel_actual = np.copy(result)
        
        return matriz_nivel_actual
    
    def inverse(self,matrix_wavelet,image_data_empty):
        matriz_recuperada = image_data_empty
        matriz_actual = np.copy(matrix_wavelet)
        
        for level in reversed(range(self.levels)): #vamos del nivel mas alto hacia el mas bajo (0)
            dimension = matriz_actual.shape[0]
            filas = matriz_actual.shape[1]//(2**level)
            columnas = matriz_actual.shape[2]//(2**level)
            
            #recorremos primero verticalmente:
            for dim in range(dimension):
                for col in range(columnas//2): #fijamos la columna
                    for fila in range(filas//2): #recorremos por filas
                        a = int(matriz_actual[dim][fila][col]) #seria la L (foto profe)
                        b = int(matriz_actual[dim][fila+filas//2][col]) #seria la H (foto profe)
                        
                        #banda LL:
                        matriz_recuperada[dim][2*fila][col] = int(b+a-(int(b/2)))
                        
                        #banda LH:
                        matriz_recuperada[dim][2*fila+1][col] = int(a-int(b/2))
                        
            matriz_actual= np.copy(matriz_recuperada)
            
            #recorremos horizontalmente:
            for dim in range(dimension):
                for fila in range(filas): #fijamos fila
                    for col in range(columnas//2): #recorremos por columnas
                        a = int(matriz_actual[dim][fila][col])
                        b = int(matriz_actual[dim][fila][col+columnas//2])
                        
                        #banda L:
                        matriz_recuperada[dim][fila][2*col] = int(b+a-(int(b/2)))
                        
                        #banda H:
                        matriz_recuperada[dim][fila][2*col+1] = int(a-int(b/2))
                        
            matriz_actual = np.copy(matriz_recuperada)
                        
        return matriz_actual
        

                
        