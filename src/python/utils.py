# -*- coding: utf-8 -*-

'''
This file contains a number of useful functions for removing duplicates.

@author: VictorioMolina
'''

from functools import reduce
import numpy as np


def remove_duplicates_1(seq):
    # Not preserving the order
    return list(set(seq))

def remove_duplicates_2(seq):
    # Preserving the order
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def remove_duplicates_3(seq):
    # Not preserving the order
    keys = {}
    for x in seq:
        keys[x] = 1
    return list(keys.keys())

def remove_duplicates_4(seq):
   # Preserving the order
   def uniquefy_list(seq):
       found = []
       for x in seq:
           if x in found:
               continue    
           found.append(x)
           yield x
               
   return list(uniquefy_list(seq))

def remove_duplicates_5(seq):
    # Preserving the order and using functools.reduce() with a lambda
    return reduce(lambda l, x: l.append(x) or l if not x in l else l, seq, [])

def remove_duplicates_6(seq):
    # Not preserving the order and using NumPy
    return list(np.unique(seq))

def remove_duplicates_7(seq):
    # Preserving the order and using NumPy
    indexes = sorted(np.unique(seq, return_index=True)[1])
    return [seq[i] for i in indexes]

def remove_duplicates_8(seq):
    # TODO - Python Wrapper for calling the C function
    pass