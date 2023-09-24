import sys
import os

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
        #TO BE IMPLEMENTED
        
    def decoding(self):
        BFI = binary_file_input(self.file_name)
        BFI.open_binay_file_input()
        #TO BE IMPLEMENTED
        
