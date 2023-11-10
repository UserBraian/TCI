import sys
import os
import numpy

#object to manipulate a input binary file
class load_image_raw:
    
     #constructor. file_name is the path of the file
    def __init__(self, image_name, components, rows, columns, datatype):
        self.image_name = image_name
        self.components = components
        self.columns = columns
        self.rows = rows
        self.datatype = datatype
        
    #open the binary file for reading
    #returns a matrix with the readed image
    def load_image_raw(self):
        image = numpy.fromfile(self.image_name, dtype=self.datatype, sep="")
        image = numpy.reshape(image, (self.components, self.rows, self.columns))
        return image
    
    #return the size in bytes of the original image
    #ALERT! cases according to >i2 must be managed
    def get_original_size_in_bytes(self):
        if self.datatype == "uint8" or self.datatype == "int8":
            bytes_sample = 1
        else:
            bytes_sample = 2
        return self.components * self.columns * self.rows * bytes_sample
    
    def get_image_structure_empty(self):
        return numpy.zeros((self.components, self.rows, self.columns))
        
