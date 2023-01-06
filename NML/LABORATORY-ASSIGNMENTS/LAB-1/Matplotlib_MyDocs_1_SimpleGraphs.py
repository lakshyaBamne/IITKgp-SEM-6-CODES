#---------------------------------------------------------------------------------------------------------
# ----------------------IMPORTANT METHODS IN MATPLOTLIB TO PLOT SIMPLE GRAPHS-----------------------------
#---------------------------------------------------------------------------------------------------------
# PART-1 : IMPORTING THE REQUIRED LIBRARIES
#---------------------------------------------------------------------------------------------------------

# pyplot is the sublibrary in matplotlib reponsible for plotting basic graphs which can be customised
import matplotlib.pyplot as plt

# NumPy methods are used to provide appropriate objects for matplotlib to plot graphs
import numpy as np

from matplotlib.figure import Figure

#---------------------------------------------------------------------------------------------------------
# PART-2 : Plotting a basic graph with given points on X-axis and Y-axis
#---------------------------------------------------------------------------------------------------------

# Points on individual axes need to be stored in python lists
x = [1,2,3,4,5]
x2 = [1,4,9,16,25]
x3 = [1,8,27,64,125]

# To create an empty figure which will be shown on the window 
# i.e. create an empty window to show something on
# create multiple to form multiple windows and do different things on them

# creating a window to show the plots on

# matplotlib.pyplot.figure() is a method which returns an empty figure window 
# which is an object of the class matplotlib.pyplot.Figure

# figsize=(width, height) //inches

myPlot_1 = plt.figure(figsize=(10,10))

# now we need a set of axes on the figure which allow us to plot a set of points

# matplotlib.pyplot.plot() is a method to plot axes on the figure (axes : X-axis + Y-axis)
# this plotting is done in the last instance of the Figure object created using pyplot.figure() method
# if we want to plot only one set of axes, pyplot.plot() and pyplot.subplot() are equivalent
plt.plot(x,x2)
plt.plot(x,x3)

# the lists which are passed as arguments for plot() must be of the same dimensions
# i.e., have a one-to-one corresponding as (x,y) coordinates

# we can create a new figure and plot axes on it in a single call in the following manner :-
myPlot_2, ax = plt.subplots()
# multiple plots can be made on the same axes by using multiple function calls following the figure object
ax.plot(x,x2)
ax.plot(x,x3)



# matplotlib.pyplot.show() is a method to show ALL the FIGURE WINDOWS along with everything present on them
plt.show()


