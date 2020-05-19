#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on Thu May  7 01:40:07 2020

@author: VictorioMolina
'''

import sys
import utils
import matplotlib.pyplot as plt
import time


# Method that turns the file into a list
def file_to_list(path):
    try:
        f = open(path, 'r')
    except IOError:
        # The file doesn't exist
        print("The file {} doesn't exists".format(path))
        sys.exit(-1)
    else:
        # The file exists
        elements = []
        for (line in f):
            elements.append(int(line.strip('\n')))
        close(f)
        return elements

def main():

    """

        ---------------------------------------------------------------------------
        PROGRAM ARGUMENTS:
            -> infile: input file with a list of elements, one per line
            -> outfile: output file where that same list of elements will be saved, 
                    but without repetitions
            -> pdf_outfile: output file where the graph that will show the time used
                    by each technique for different data sizes will be saved in pdf
        ---------------------------------------------------------------------------

    """

    # Command line argument control
    if len(sys.argv) != 4:
        print("Usage: {} infile outfile pdf_outfile".format(sys.argv[0]))
        sys.exit(0)


    # Reading the sequence of the input file
    seq = file_to_list(sys.argv(1))

    # Calling the external function through its wrapper, with the corresponding time taking
    t0 = time.time_ns()
    out_arr = utils.remove_duplicates_8(seq)
    t_exec = (time.time_ns() - t0) / 1.0e9
    print("The C removal duplicates function has taken {} seconds to execute.".format(t_exec))

if __name__ == '__main__':
    main()
