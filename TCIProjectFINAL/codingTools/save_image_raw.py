import sys
import os

from .binary_file_output import *
from .save_image_raw import *

#object to manipulate a input binary file
class save_image_raw:
    
     #constructor. file_name is the path of the file
    def __init__(self, image_name):
        self.image_name = image_name       
    
    #saves the image_data content into the binary file in BigEndia
    def save_image_raw(self, image_data, dtype):
        if dtype == "uint8" or dtype == "int8":
            bits_to_write = 8
        else:
            bits_to_write = 16
            
        BFO = binary_file_output(self.image_name)
        BFO.open_binay_file_output()
        for z in range(image_data.shape[0]):
            for y in range(image_data.shape[1]):
                for x in range(image_data.shape[2]):
                    BFO.write_value(int(image_data[z][y][x]),bits_to_write)
        BFO.close_binary_file_output()
        