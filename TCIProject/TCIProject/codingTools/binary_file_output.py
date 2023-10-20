import sys
import os

from .utils import *
#object to manipulate a output binary file
class binary_file_output:
    
    #constructor. file_name is the path of the file
    def __init__(self, file_name):
        self.file_name = file_name
        self.byte = 0
        self.counter_bit = 0
        self.counter_bytes = 0

    #open the binary file for writting
    def open_binay_file_output(self):
        self.binary_file = open(self.file_name, "wb")
        print('open ok')
        
    #close the object of the binary file
    def close_binary_file_output(self):
        while self.counter_bit != 0:
            self.write_bit(0)
        self.binary_file.flush()
        self.binary_file.close()

    #writes a bit into a byte. When the byte is full it written to the file, then empty the byte.
    def write_bit(self, bit):
        self.counter_bit += 1
        self.byte = self.byte | (bit << (8 - self.counter_bit))


        if self.counter_bit == 8:
            #print("writting a byte")
            self.binary_file.write(self.byte.to_bytes(1,'big'))
            self.counter_bit = 0
            self.byte = 0
            self.counter_bytes += 1

    #write the value employing the bits of num_of_bits. It employs the write_bit(self,bit)
    def write_value(self, value, num_of_bits):
        #TO BE IMPLEMENTED -- DONE
        #value: valor que queremos esccribir --> 10 -> binario: 1010
        #num of bits: bits que representan el value -->  4bits
        #Recorremos el binario de izq a der
            
        num = num_of_bits
        
        for _ in range(num-1,-1,-1):
            bit = (value>> _)&1
            self.write_bit(bit)
        
    def size_of_file(self):
        return(self.counter_bytes)
