import sys
import os
from .utils import *


#object to manipulate a input binary file
class binary_file_input:
    
    #constructor. file_name is the path of the file
    def __init__(self, file_name):
        self.file_name = file_name
        self.byte = 0
        self.counter_bit = 0

    #open the binary file for reading
    def open_binay_file_input(self):
        self.binary_file = open(self.file_name, "rb")
        print('open ok')
    
    #returns the readed bit
    def read_bit(self):
        if self.counter_bit == 0:
            self.readed_byte = self.binary_file.read(1) #el byte en binario
            self.readed_byte_int = int.from_bytes(self.readed_byte, byteorder='big', signed=False) #el byte en entero
            self.counter_bit = 8
        self.counter_bit -= 1
        readed_bit = 1 if (self.readed_byte_int & (1 << (self.counter_bit))) != 0 else 0
        return readed_bit

    #return the value readed according on num_of_bits
    def read_value(self, num_of_bits):
        value = 0
        ######TO BE IMPLEMENTED
        
        for i in range(num_of_bits):
            v=self.read_bit()
            #print('bit leido:',v)
            value= (value<<1)|v
            
        return value