#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Created on Thu May  7 01:40:07 2020

@author: VictorioMolina
'''

import sys
import utils
import matplotlib.pyplot as plt
import numpy as np
import time
from inspect import getmembers, isfunction
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec

plt.rcParams.update({'font.size': 14})
plt.rcParams.update({'figure.max_open_warning': 0})


# Method that turns the file lines into a list
def file_to_list(path):
    try:
        infile = open(path, 'r')
    except IOError:
        # The file doesn't exist
        print("The file {} doesn't exists".format(path))
        sys.exit(-1)
    else:
        # The file exists
        elements = []
        
        # Add the file lines to the list of elements
        elements.extend(int(line) for line in infile)

        infile.close()
        return elements

# Method that writes the result of the program in an specific file
def result_to_file(result, path):
    try:
        outfile = open(path, 'x')
    except FileExistsError:
        print("The file {} already exists".format(sys.argv[2]))
        sys.exit(-1)
    else:
        # Salvar en un fichero de texto con la «cabecera» dada:
        for element in result:
            outfile.write(str(element) + '\n')
        outfile.close()

# Method that generates a plot and save it in an specific PDF file
def generate_plots(title, x, y, pdf):
    fig = plt.figure(figsize=(14, 19.8)) # A4 Size

    fig.suptitle(title, fontsize=30)

    spec = gridspec.GridSpec(ncols=3, nrows=2, width_ratios=[0.5,4,0.5])

    # Bar plot
    ax = fig.add_subplot(spec[1])
    plt.xlabel("Execution Time")
    width = 0.75 # Bars' width
    ind = np.arange(len(y))
    ax.barh(ind, y, width, color="blue")
    ax.set_yticks(ind + width / 4)
    ax.set_yticklabels(x, minor=False)

    # Pie chart
    ax1 = fig.add_subplot(spec[4])
    explode = (0, 0, 0, 0, 0, 0.05)  # only "explode" the 6th slice which represents the C function
    ax1.pie(
        [_ * 1000 for _ in y],
        explode=explode,
        labels=x,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90
    )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save current figures in a pdf page
    pdf.savefig()



# Method that studies the efficiency of each technique for different data sizes
# generating graphics that will be saved in a pdf
def study_techniques_efficiency(seq, path):
    try:
        pdf_outfile = open(path, 'x')
    except FileExistsError:
        print("The file {} already exists".format(path))
        sys.exit(-1)
    else:
        # Create a multipage PDF file
        pdf = PdfPages(path)

        # Get all the functions of the module
        functions_list = [o for o in getmembers(utils, isfunction)]
        
        # Make an study of each technique in size intervals of 2000 elements
        size_interval = 2000
        for i in range(int(len(seq) / size_interval)):
            # For each technique, calling its function with the corresponding time taking
            cutten_list = seq[0:(i+1)*size_interval]
            exec_times = [] # Will store the exec time of each function 

            for function_name, function_obj in functions_list:
                # Calculate the exec time
                t0 = time.time_ns()
                result = function_obj(cutten_list)
                t_exec = (time.time_ns() - t0) / 1.0e9

                # Store the ecex time
                exec_times.append(t_exec)
                print("{} has taken {} seconds to execute".format(function_name, t_exec))

            # Generate a plot with the execution time stats
            generate_plots(
                    "TIMES FOR THE FIRST {} NUMBERS".format((i+1)*size_interval),
                    [f[0] for f in functions_list],
                    exec_times,
                    pdf
            )
        
        # Close the pdf
        pdf.close()

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
    seq = file_to_list(sys.argv[1])

    # Calling the external function through its wrapper
    result = utils.remove_duplicates_6(seq)

    # Writing the result in the outfile
    result_to_file(result, sys.argv[2])

    # Finally, study the different techniques efficiency
    study_techniques_efficiency(seq, sys.argv[3])

if __name__ == '__main__':
    main()
