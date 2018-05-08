# -*- coding: utf-8 -*-
"""

This script is designed to plot the total mass of particles in the pulp lifter
over the simulated time

Author: Dr Wei Chen
Design Engineer - DEM
GCC - Bradken

wchen@bradken.com

"""
from paraview.simple import *

# loop through the time step range to save the screenshots
for i in range(1, 1000):
    # animate the scene
    animationScene1 = GetAnimationScene()
    # go to next frame
    animationScene1.GoToNext()
    # get current all views layout
    aLayout = GetLayout()
    # create the image name
    file_name = "AllViewsImage_" + str(i) + ".png"
    # save screenshots recursively
    SaveScreenshot(file_name, layout=aLayout)
