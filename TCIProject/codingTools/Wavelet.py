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
        matriz_nivel_actual = self.original_image
        
        #Hay que comprobar que la num de columnas sea un numero par, sino habra que replicar la ultima columna y añadirla a la matriz (imagen)
        #if((m%2)!=0):
        #    kk=1
            #get ultima columna de la imagen
            #añadir columna a matriz -> sth like reshape matriz
            
        
        a = 0
        b = 0
        print('matriz actual: \n',matriz_nivel_actual)
        
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
                        
            print('result horizontal: \n',result) #Valores correctos (checked)  result ahora es la matriz : L|H
            
            matriz_nivel_actual = np.copy(result)
            
                
            #Forward vertical - Trabaja solo con la banda L y nos genera la matriz LL|H
            #                                                                      LH|H
            for z in range(matriz_nivel_actual.shape[0]):
                for j in range(matriz_nivel_actual.shape[2]//2): #Columnas (fijamos columna)
                    for i in range(matriz_nivel_actual.shape[1]//2): #Filas (movemos por cada fila)
                        a_L = int(matriz_nivel_actual[z][2*i][j])
                        #print('a: ',a_L)
                        b_L = int(matriz_nivel_actual[z][2*i+1][j])
                        #print('b: ',b_L)
                        
                        op1 = b_L+int(int(a_L-b_L)/2)
                        #print('b + a-b/2 -> op1: ',op1)
                        
                        op2 = int(a_L-b_L)
                        #print('a-b -> op2: ',op2)
                
                        #banda LL:
                        result[z][i][j] = b_L+int(int(a_L-b_L)/2)
                        
                        #banda LH:
                        result[z][i+filas//2][j] = int(a_L-b_L)
            
                
                        
            print('result vertical: \n',result) #Valores correctos (checked) result ahora es la matriz : LL|H
            #                                                                                            LH|H
            
            matriz_nivel_actual = np.copy(result)

                
        
