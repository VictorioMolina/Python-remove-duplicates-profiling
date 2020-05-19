# -*- coding: utf-8 -*-

'''
This file contains a number of useful functions for removing duplicates.

@author: VictorioMolina
'''

import ctypes, os
from functools import reduce
import numpy as np
import time


# Loading the shared library into ctypes
LIBREMOVE_DUPLICATES = ctypes.CDLL(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../C/libremove_duplicates.so.1")
    )
)

# @profile
def remove_duplicates_1(seq):
    # Not preserving the order
    return list(set(seq))

# @profile
def remove_duplicates_2(seq):
    # Preserving the order
    found = set()
    return [x for x in seq if not (x in found or found.add(x))]

# @profile
def remove_duplicates_3(seq):
    # Not preserving the order
    keys = {}
    for x in seq:
        keys[x] = 1
    return list(keys.keys())

# @profile
def remove_duplicates_4(seq):
    # Not preserving the order and using NumPy
    return list(np.unique(seq))

# @profile
def remove_duplicates_5(seq):
    # Preserving the order and using NumPy
    indexes = sorted(np.unique(seq, return_index=True)[1])
    return [seq[i] for i in indexes]

# Python Wrapper for calling the C function
# @profile
def remove_duplicates_6(seq):    
    # Object corresponding to the function within the library
    func_remove_duplicates = LIBREMOVE_DUPLICATES.remove_duplicates
    
    # Function protoype
    func_remove_duplicates.argtypes = [
        ctypes.POINTER(ctypes.c_uint),
        ctypes.POINTER(ctypes.c_uint),
        ctypes.c_uint
    ]
    
    # This function returns void
    func_remove_duplicates.restype = None

    # Variable in which we will collect the result of the function.   
    result = (ctypes.c_uint * len(seq))()
    
    # Call to the shared library function.
    func_remove_duplicates((ctypes.c_uint * len(seq))(*seq), result, len(seq))
    
    # Copying result of the function to another vector
    vout=[*result]  # This type of copy is the 'fastest' in Python
        
    # Removing all zeros least the first one
    while len(vout) > 1 and vout[-1] == 0:
        vout.pop()
        
    # Finally, we return the output vector
    return vout
