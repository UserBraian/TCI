import sys
import math

#returns the needed bits to represent value in binary
def needed_bits(value):
    if value == 0:
        needed_bits = 1
    else:
        needed_bits = math.ceil(math.log(value)/math.log(2))
    return needed_bits
 
def sign_of_value(value):
    if value < 0 : return (-1)
    else : return (1)

def abs_of_value(value):
    return math.abs(value)