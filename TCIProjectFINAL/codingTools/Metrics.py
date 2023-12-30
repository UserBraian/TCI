import sys
import os
import math

from .utils import *

#object to quantize/dequantize input data
class Metrics:
    
    #constructor. 
    def __init__(self, original_image, reconstructed_image):
        self.original_image = original_image
        self.reconstructed_image = reconstructed_image
        self.MSE = 0
        self.PSNR = 0
        self.PAE= 0
        
        self.original_image_components = original_image.shape[0]
        self.original_image_rows = original_image.shape[1]
        self.original_image_columns = original_image.shape[2]
        
        self.reconstructed_image_components = reconstructed_image.shape[0]
        self.reconstructed_image_rows = reconstructed_image.shape[1]
        self.reconstructed_image_columns = reconstructed_image.shape[2]
        
        #DIMENSIONS OF BOTH IMAGES NEED TO BE VALIDATED
    def needed_bits(self, value):
        if value == 0:
            needed_bits = 1
        else:
            needed_bits = math.ceil(math.log(value)/math.log(2))
        return needed_bits
    #Check the geometry of the images to be compared
    def check_geometry(self):
        if  self.original_image_rows==self.reconstructed_image_rows and self.reconstructed_image_columns==self.original_image_columns:
            return True
        else:
            return False
        
    
    #compute metrics    
    def compute(self):
        if self.check_geometry()==True:
            maxval=0
            maxvalPAE=0
            suma=0
            
            for z in range(self.original_image.shape[0]):
                for i in range(self.original_image.shape[1]):
                    for j in range(self.original_image.shape[2]):
                        m=self.original_image[z][i][j]
                        n=self.reconstructed_image[z][i][j]
                        res=abs(m-n)
                        suma=suma+((m-n))**2
                        if maxval<=n:
                            maxval=n
                        if maxvalPAE<=res:
                            maxvalPAE=res
                        
                            
                        
                    

            bits = self.needed_bits(maxval)
            print("bits", bits)
            
            self.MSE=1/(self.original_image_rows* self.original_image_columns)*suma
            self.PSNR=10*math.log10((((2**bits)-1)**2)/self.MSE)
            self.PAE=maxvalPAE
            
            print("MSE=", self.MSE)
            print("PSNR=", self.PSNR)
            print("PAE=", self.PAE)
        else:
            print("no son iguales")
            
    
