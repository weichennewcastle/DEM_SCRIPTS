# -*- coding: utf-8 -*-
"""

This script is designed to plot the total mass of particles in the pulp lifter
over the simulated time

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

def main():
    # Get the dump liggghts list and rearrange with time
    png_list = glob.glob('side_*.png')
    png_list.sort(key=os.path.getmtime)

    st = 31
    for png_f in png_list:
        f_name = 'side_00' + str(st) + '.png'
        os.rename(png_f, f_name)
        st += 1

    for rp in range(1, 31):
        ff_name = 'side_00' + str(rp) + '.png'
        os.rename('side_01.png', ff_name)


if __name__ == "__main__":
    main()





