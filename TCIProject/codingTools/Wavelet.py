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
    
        filas=self.original_image.shape[1]
        columnas=self.original_image.shape[2]//2
        print("f:", filas)
        print("c", columnas)
        L=np.empty((filas,columnas))
        H=np.empty((filas,columnas))
        
        a = 0
        b = 0
        
        for z in range(self.original_image.shape[0]):
            for i in range(self.original_image.shape[1]):
                for j in range((self.original_image.shape[2]//2)): 
                    a=int(self.original_image[z][i][2*j])
                    b=int(self.original_image[z][i][2*j+1])
                    op=b+int(int(a-b)/2)
               
                    L[i][j]=op
                    H[i][j]=(a-b)
                    
        for z in range(self.original_image.shape[0]):
            for j in range(self.original_image.shape[2]): 
                for i in range((self.original_image.shape[1]//2)-1):
                    a=self.original_image[z][2*i][j]
                    b=self.original_image[z][2*i+1][j]
                    #Lv.append(b+((a-b)//2))
                    #Hv.append(b-a)
                    
        print(L)
        print(H)
        
    
    
    
    

