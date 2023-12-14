import sys
import os
import numpy as np
import math

class Prediction:
    
    
    def __init__(self,image):
        self.original_image = image
    
    def east_pred(self, empty_image):
        #P_east[][] = X[i][j] - X[i][j-1]
        dimension = self.original_image.shape[0]
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]
        result = np.copy(empty_image)
        
        for dim in range(dimension):
            for i in range(filas):
                for j in range(columnas):
                    if j==0:
                        result[dim][i][j] = int(self.original_image[dim][i][j])
                    else:
                        actual = int(self.original_image[dim][i][j])
                        anterior = int(self.original_image[dim][i][j-1])
                        result[dim][i][j] = int(actual-anterior)
        
        return result
    
    def north_and_east(self, empty_image):
        #P_east[][] = X[i][j] - X[i][j-1]
        dimension = self.original_image.shape[0]
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]
        result = np.copy(empty_image)
        
        for dim in range(dimension):
            for i in range(filas):
                for j in range(columnas):
                    if j==0 or j==1 or i==0 or i==1:
                        result[dim][i][j] = int(self.original_image[dim][i][j])
                    else:
                        actual = int(self.original_image[dim][i][j])
                        anterior_col1 = int(self.original_image[dim][i][j-1])
                        anterior_fila1 = int(self.original_image[dim][i-1][j])
                        anterior_diagonal1 = int(self.original_image[dim][i-1][j-1])
                        
                        anterior_col2 = int(self.original_image[dim][i][j-2])
                        anterior_fila2 = int(self.original_image[dim][i-2][j])
                        anterior_diagonal2 = int(self.original_image[dim][i-2][j-2])
                        
                        result[dim][i][j] = int(actual-int((2*anterior_col1+1.5*anterior_fila1+1*anterior_diagonal1+2*anterior_col2+1.5*anterior_fila2+1*anterior_diagonal2)/9))
        
        return result
    
    def north(self, empty_image):
        #P_east[][] = X[i][j] - X[i][j-1]
        dimension = self.original_image.shape[0]
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]
        result = np.copy(empty_image)
        
        for dim in range(dimension):
            for i in range(filas):
                for j in range(columnas):
                    if i==0:
                        result[dim][i][j] = int(self.original_image[dim][i][j])
                    else:
                        actual = int(self.original_image[dim][i][j])
                        anterior = int(self.original_image[dim][i-1][j])
                        result[dim][i][j] = int(actual-anterior)
        
        return result
    
    def northeast(self, empty_image):
        #P_east[][] = X[i][j] - X[i][j-1]
        dimension = self.original_image.shape[0]
        filas = self.original_image.shape[1]
        columnas = self.original_image.shape[2]
        result = np.copy(empty_image)
        
        for dim in range(dimension):
            for i in range(filas):
                for j in range(columnas):
                    if j==0 and i==0:
                        result[dim][i][j] = int(self.original_image[dim][i][j])
                    else:
                        actual = int(self.original_image[dim][i][j])
                        anterior = int(self.original_image[dim][i-1][j-1])
                        result[dim][i][j] = int(actual-anterior)
        
        return result
        
    
    
    def GodPrediction(self, empty_image):
        image_data_empty = ImageRaw.get_image_structure_empty()
        pred1 = Prediction(original_image)
        imagen_prima1 = pred1.north_and_east(image_data_empty)
        residu1 = original_image-imagen_prima1
    
        q=Quantizer(1,10)
        img_q=ImageRaw.get_image_structure_empty()
        q.quantize(residu1, img_q)
        
        img_desq=ImageRaw.get_image_structure_empty()
        q.dequantize(img_q, img_desq)
        
        dimension = img_desq.shape[0]
        filas = img_desq.shape[1]
        columnas = img_desq.shape[2]
        result = np.copy(empty_image)
        
        p=ImageRaw.get_image_structure_empty()
        x_barret=ImageRaw.get_image_structure_empty()
        
        for dim in range(dimension):
            for i in range(filas):
                for j in range(columnas):     
                    if j==0:
                        p[dim][i][j]=0
                    else:                      
                        p[dim][i][j]=p[dim][i][j-1]+img_desq[dim][i][j]
        
        
        x_barret=img_desq+p
        
        return x_barret
    
    def LiniaPrincipal(self, x_barret):
        
        image_data_empty = ImageRaw.get_image_structure_empty()
        pred1 = Prediction(x_barret)
        imagen_prima1 = pred1.north_and_east(image_data_empty)
        residu1 = original_image-imagen_prima1
    
        q=Quantizer(1,10)
        img_q=ImageRaw.get_image_structure_empty()
        q.quantize(residu1, img_q)
        
        img_desq=ImageRaw.get_image_structure_empty()
        q.dequantize(img_q, img_desq)
        
        aux_img=img_desq+imagen_prima1
        m=Metrics(self.original_image, aux_img)
        m.compute()
        
        return aux_img
