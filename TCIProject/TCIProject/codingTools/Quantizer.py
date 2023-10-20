import sys
import os

from .utils import *

#object to quantize/dequantize input data
class Quantizer:
    
    #constructor. 
    def __init__(self, quantizer_technique, quantization_step):
        self.quantizer_technique = quantizer_technique
        self.quantization_step = quantization_step
        
    #quantize    
    def quantize(self, image_data, image_data_quantized):
        for z in range(image_data.shape[0]-1):
            for y in range(image_data.shape[1]-1):
                for x in range(image_data.shape[2]-1):
                    image_data_quantized[z][y][x] = int(sign_of_value(image_data[z][y][x]) * (image_data[z][y][x] / self.quantization_step))                
        
    #dequantize
    def dequantize(self, image_data_quantized, image_data_reconstructed):
        for z in range(image_data_quantized.shape[0]-1):
            for y in range(image_data_quantized.shape[1]-1):
                for x in range(image_data_quantized.shape[2]-1):
                    image_data_reconstructed[z][y][x] = image_data_quantized[z][y][x] * self.quantization_step
                    
    

    