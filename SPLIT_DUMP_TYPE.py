# -*- coding: utf-8 -*-
"""

This script is designed to split the LIGGGHTS dump results into different files
based on the "type" property

Author: Dr Wei Chen
Design Engineer - DEM
GCC - Bradken

wchen@bradken.com

"""

import os
import glob
import math
import pandas as pd

#import matplotlib.pyplot as plt
import numpy as np

def SPLIT_DUMP(header, body, liggghts_file):
    # get the file name first
    water_dump_name = 'dump_water_' + liggghts_file[5:]
    ore_dump_name = 'dump_ore_' + liggghts_file[5:]
    # bind header with body
    water_f = open(water_dump_name, 'w')
    ore_f = open(ore_dump_name, 'w')
    # Loop through lines and write ore & water separately
    cnt_ore = 0             # Counter for total ore particles
    cnt_water = 0           # Counter for total water particles
    for line in body:
        tmp_a = line.strip('\n')
        tmp_b = tmp_a.split()
        tmp_c = [float(a) for a in tmp_b]
        if tmp_c[1] == 1:
            # ore particle line
            cnt_ore += 1
        else:
            # water particle line
            cnt_water += 1
    # Change header first
    water_header = header
    ore_header = header

    cnt_a = 1
    cnt_b = 1
    for line in body:
        tmp_a = line.strip('\n')
        tmp_b = tmp_a.split()
        tmp_c = [float(a) for a in tmp_b]
        if tmp_c[1] == 1:
            # ore particle line
            tmp_b[0] = str(cnt_a)
            cnt_a += 1
            wrt_a = [' '.join(tmp_b) + '\n']
            ore_header = ore_header + wrt_a
        else:
            # water particle line
            tmp_b[0] = str(cnt_b)
            cnt_b += 1
            wrt_b = [' '.join(tmp_b) + '\n']
            water_header = water_header + wrt_b
    # Close the files first
    water_header[3] = str(cnt_water) + '\n'
    ore_header[3] = str(cnt_ore) + '\n'
    water_f.writelines(water_header)
    ore_f.writelines(ore_header)
    water_f.close()
    ore_f.close()
    return

def main():
    # Get the dump liggghts list and rearrange with time
    lig_list = glob.glob('dump_*.liggghts')
    lig_list.sort(key=os.path.getmtime)

    for lig_f in lig_list:
        # Read the file
        fop = open(lig_f, 'r')
        # Read all lines
        lines = fop.readlines()
        # get the header
        header = lines[0:9]
        #print(header)
        # get particle information
        body = lines[9:]
        # filter liner based on the type property, using a function
        SPLIT_DUMP(header, body, lig_f)

if __name__ == "__main__":
    main()