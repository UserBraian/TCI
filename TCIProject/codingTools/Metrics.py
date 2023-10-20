import sys
import os

from .utils import *

#object to quantize/dequantize input data
class Metrics:
    
    #constructor. 
    def __init__(self, original_image, reconstructed_image):
        self.original_image = original_image
        self.reconstructed_image = reconstructed_image
        self.MSE = 0
        self.PSNR = 0
        
        self.original_image_components = original_image.shape[0]
        self.original_image_rows = original_image.shape[1]
        self.original_image_columns = original_image.shape[2]
        
        self.reconstructed_image_components = reconstructed_image.shape[0]
        self.reconstructed_image_rows = reconstructed_image.shape[1]
        self.reconstructed_image_columns = reconstructed_image.shape[2]
        
        #DIMENSIONS OF BOTH IMAGES NEED TO BE VALIDATED
    
    #Check the geometry of the images to be compared
        if  self.original_image_rows==self.reconstructed_image_rows && self.reconstructed_image_columns==self.original_image_columns:
            return true
        else:
            return false
        pass
    
    #compute metrics    
    def compute(self):
        if check_geometry(self)==ture:
             maxval=0
            for i in self.original_image_rows:
                for j in self.original_image_columns:
                    m=self.original_image[i][j]
                    n=self.reconstructed_image[i][j]
                    if maxval<n:
                        maxval=n
                    suma=suma+(m-n)2

            bits=utils.needed_bits(maxval)
            self.MSE=1/(self.original_image_rows* self.original_image_columns)*suma

            self.PSNR=10*math.log10((((2**bits)-1)**2)/self.MSE)
        else:
            print("no son iguales")
            
       
            
        
        pass
    
