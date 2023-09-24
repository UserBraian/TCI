import sys
import os
import math

from .utils import *

#object to compute statistics of the input data
class statistics:
    
    #constructor. 
    def __init__(self, image):
        self.image = image
        self.entropy = 0
        self.max_value = 0
        self.min_value = 0
        self.dynamic_range = 0
        
        self.image_components = image.shape[0]
        self.image_rows = image.shape[1]
        self.image_columns = image.shape[2]
        self.counter = self.image_components * self.image_rows * self.image_columns
    
    #compute metrics    
    def compute_entropy(self):
   
        histogram = {}
        
        #histogram[self.image[z][y][x]]
        #TO BE IMPLEMENTED
        #for y in range(self.image_rows):
          #  for x in range(self.image_columns):
          #      a.append(self.image[y][x])
        for z in range(self.image_components):
            for y in range(self.image_rows):
                for x in range(self.image_columns):
                    if self.image[z][y][x] in histogram:
                        histogram[self.image[z][y][x]]+=1
                    else:
                        histogram[self.image[z][y][x]]=1
         ### ok  
                
        probs={}
        for key in histogram.keys():
            probs[key]=histogram[key]/self.counter
            
        for key in probs.keys():
            self.entropy+=probs[key]*math.log2(1/(probs[key]))
            
        return self.entropy
                               