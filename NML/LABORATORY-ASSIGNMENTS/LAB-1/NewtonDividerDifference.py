# Implementation of the Newton's Divider Differences Interpolation method
#	-> GIVEN A SET OF n+1 COORDINATES, FIND AN nth DEGREE POLYNOMIAL THAT PASSES THROUGH THESE POINTS
#	-> FIND THE EQUATION OF THE POLYNOMIAL AND GIVE VALUE OF THE POLYNOMIAL ON ANY OTHER ARBITRARY POINT
#	-> PLOT THE GRAPH FOR THE FOUND POLYNOMIAL USING ANY TECHNOLOGY

#---------------------------------------------------------------------------------------------------------
# IMPORTING REQUIRED LIBRARIES

import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------------------------------
# FUNCTION DEFINITIONS

# Function to find the HIGHEST COEFFICIENT of an nth degree polynomial given n+1 data points
# Function is based on Divide & Conquer Technique
def _NewtonDividerDifferences_(vectorXn, vectorYn, leftIndex, rightIndex):
    if leftIndex+1 == rightIndex:
        # base case and also the conquer step
        return ( vectorYn[rightIndex] - vectorYn[leftIndex] )/( vectorXn[rightIndex] - vectorXn[leftIndex] )

    # if it is not base case, the divide step is performed

    # The main problem is divided to two problems according to the rules of
    # Newton's Divider Differences Method
    first = _NewtonDividerDifferences_( vectorXn, vectorYn, leftIndex+1, rightIndex )
    second = _NewtonDividerDifferences_( vectorXn, vectorYn, leftIndex, rightIndex-1 )
    
    numerator = first - second
    denominator = vectorXn[rightIndex] - vectorXn[leftIndex]
    finalValue = numerator / denominator

    return finalValue

# function to find the value for a new point entered by the user
def _NewPoint_(new_X_coordinate, coeffList, vector_Xn):
    finalValue = coeffList[0]

    for i in range(1, len(coeffList)):
        newProd = 1
        for j in range(0, i):
            newProd = newProd * ( new_X_coordinate - vector_Xn[j] )

        finalValue = finalValue + ( coeffList[i] * newProd )
    
    return finalValue

#---------------------------------------------------------------------------------------------------------
# PROGRAM STARTS IMPLEMENTATION FROM HERE

# variable to store the number of data points entered by the USER
numPoints = int(input("Enter the number of Data Points : "))

print("--------------------------------------------------------------------------------------")

# Lists to take the Data points as Input
vectorXn = []
vectorYn = []

# Taking input into the lists from the user
print("Enter the X coordinates :- ")
for i in range(numPoints):
    tempVar = float(input(f"x{i} : "))
    vectorXn.append( tempVar )

print("--------------------------------------------------------------------------------------")

print("Enter the Y coordinates :- ")
for i in range(numPoints):
    tempVar = float(input(f"y{i} : "))
    vectorYn.append( tempVar )

print("--------------------------------------------------------------------------------------")

# new empty vectors to calculate one diagonal element at a time
newXvector = []
newYvector = []

# the first coefficient is always the first element in vectorYn
newXvector.append( vectorXn[0] )
newYvector.append( vectorYn[0] )

# List to store the coefficients in the order a0,a1,a2,....,an
CoeffList = []

CoeffList.append( vectorYn[0] )

# iterations to calculate the coefficients

for i in range(1, numPoints):
    newXvector.append( vectorXn[i] )
    newYvector.append( vectorYn[i] )

    coeffValue = _NewtonDividerDifferences_( newXvector, newYvector, 0, i )

    CoeffList.append(coeffValue)

# Printing the coefficients for the found polynomial
print(f"Coefficients of the {numPoints-1}th degree polynomial are :-")
for i in range(numPoints):
    print(f"a{i} = {CoeffList[i]}")

print("--------------------------------------------------------------------------------------")

newPoint = float(input("Enter the new Point to calculate value : "))

print(f"New coordinate is : ( {newPoint} , {_NewPoint_(newPoint, CoeffList, vectorXn)} )")

print("--------------------------------------------------------------------------------------")

#---------------------------------------------------------------------------------------------------------
# PLOTTING THE GRAPHS

# Now we need to plot the polynomial curve whose equation is known to us with coefficients
# in the CoeffList vector
# first we need sufficient points in a list to plot on the x-axis

# we want the Data Points to be in the plot so we use them to calculate the range

leftRange = vectorXn[0]
rightRange = vectorXn[0]

# finding the minimum and maximum elements in the vector of x-coordinates
for i in range(1, numPoints):
    if vectorXn[i]<leftRange:
        leftRange = vectorXn[i]
    if vectorXn[i]>rightRange:
        rightRange = vectorXn[i]

# increasing the range for more points to be plotted and better visualization
leftRange = leftRange - 1.0
rightRange = rightRange + 1.0

# creating the list of points on which the graph will be plotted
x = np.linspace( leftRange, rightRange , 1000)
y = []

# using the _NewPoint_ function to find the value given by the found polynomial
#  at the points in x-axis vector
for i in x:
    newPoint_Y = _NewPoint_(i, CoeffList, vectorXn)
    y.append( newPoint_Y )

# creating a Figure window object to show the axes
myPlot = plt.figure(figsize=(10,10))

plt.grid()

# Plotting the original points entered by the user
plt.plot(vectorXn, vectorYn, marker="o", markersize=5, linestyle='None', label="Initial Data Points")
# Plotting the curve found by using coefficients given by Newton's Divider Difference Interpolation Method
plt.plot(x,y, label="Interpolated Polynomial Curve")

# legend to identify the different colored components

plt.legend(bbox_to_anchor =(0.75, 1.15), ncol = 2)

plt.show()

# ------------------------------------------------------END------------------------------------------------