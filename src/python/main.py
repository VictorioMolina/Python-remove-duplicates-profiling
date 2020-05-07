#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on Thu May  7 01:40:07 2020

@author: VictorioMolina
'''

import sys
import utils
import matplotlib.pyplot as plt


def main():   
    # Command line argument control
    if len(sys.argv) != 4:
        print("Usage: {} infile outfile pdf_outfile".format(sys.argv[0]))
        sys.exit(0)
        
if __name__ == '__main__':
    main()
