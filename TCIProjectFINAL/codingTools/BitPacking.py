import sys
import os

import numpy as np

from .utils import *
from .binary_file_output import *
from .binary_file_input import *

#object to manipulate a output binary file
class BitPacking:
    
    #constructor. 
    def __init__(self, file_name, image_data):
        self.file_name = file_name
        self.image_data = image_data
        self.components = image_data.shape[0]
        self.rows = image_data.shape[1]
        self.columns = image_data.shape[2]
        self.size_of_coded_file = 0

    def coding(self):
        BFO = binary_file_output(self.file_name)
        BFO.open_binay_file_output()
        #TO BE IMPLEMENTED - DONE (works?)
        
        for dim in range(self.components):
            for fila in range(self.rows):
                for col in range(self.columns):
                    value = int(self.image_data[dim][fila][col])
                    BFO.write_value(value,8)
        BFO.close_binary_file_output()
        
    def decoding(self):
        BFI = binary_file_input(self.file_name)
        BFI.open_binay_file_input()
        #TO BE IMPLEMENTED
        image_data_empty = np.zeros((self.components, self.rows, self.columns))
        
        for dim in range(self.components):
            for fila in range(self.rows):
                for col in range(self.columns):
                    image_data_empty[dim][fila][col] = BFI.read_value(8)
        
        return image_data_empty