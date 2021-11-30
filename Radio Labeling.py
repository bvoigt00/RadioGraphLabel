#############
## Imports ##
#############

import math
import numpy

##############
## Examples ##
##############

g1 = [
  [1, 2],
  [0, 3],
  [0, 3, 4, 6],
  [1, 2, 5, 7],
  [2, 5],
  [3, 4],
  [2, 7],
  [3, 6]
]
l1 = [4, 7, 1, 10, 6, 3, 8, 5]

g2 = [
  [2],
  [2],
  [0, 1, 3, 4],
  [2],
  [2]
]
l2 = [6, 3, 1, 4, 5]

g3 = [
  [1, 2, 3],
  [0, 2, 3],
  [0, 1, 3],
  [0, 1, 2]
]
l3 = [4, 1, 3, 2]

g4 = [
  [1, 2, 3],
  [0, 2, 4],
  [0, 1, 3, 4],
  [0, 2, 4],
  [1, 2, 3]
]
l4 = [7, 4, 1, 3, 6]

g5 = [
  [1],
  [0, 2],
  [1, 3],
  [2]
]
l5 = [4, 1, 6, 3]

#########################
## Starting Conditions ##
#########################

graph = g5
proposedLabeling = l5

lineLength = 6

detailedDebug = False

########################
## Method Declaration ##
########################

def main():
  lineRadioLabeling = generateRadioLabelingForLine(lineLength)
  lineRadioNumber = numpy.amax(lineRadioLabeling)
  print(f"The radio number for a path consisting of {lineLength} vertices is {lineRadioNumber}")

  isValid = checkValidLabeling(graph, proposedLabeling)
  if isValid:
    print("The proposed labeling is a valid radio labeling")
  else:
    print("The proposed labeling is not a valid radio labeling")


# Floyd's Algorithm
# Return a 2D array
def distanceMatrix(graph):
  # Initialize to infinity
  order = len(graph)
  distance = numpy.full((order, order), numpy.inf)
  # Set distance from vertex to itself as 0
  for i in range(order):
    for j in range(order):
      if i == j:
        distance[i][j] = 0
  # Set distance for adjacent vertices to 1
  for i in range(order):
    for j in range(len(graph[i])):
      distance[i][graph[i][j]] = 1
  # Main loop
  for k in range(order):
    for i in range(order):
      for j in range(order):
        if distance[i][j] > distance[i][k] + distance[k][j]:
          distance[i][j] = distance[i][k] + distance[k][j]

  return distance

def printGraph(graph):
  for v in graph:
    for a in v:
      print(int(a), end=" ")
    print()

def checkValidLabeling(graph, labeling):
  order = len(graph)
  if order != len(labeling):
    print("The labeling must contain an element for each vertex in the graph")
    return
  
  distance = distanceMatrix(graph)
  diameter = numpy.amax(distance)

  if detailedDebug:
    print("Distance Matrix")
    printGraph(distance)
    print("Diameter of testGraph")
    print(int(diameter))

  isValid = True
  for i in range(order):
    for j in range(order):
      if i != j:
        radioDifference = numpy.abs(labeling[i] - labeling[j])
        constraintCheck = diameter + 1 - distance[i][j]
        if detailedDebug:
          print("Coords: " + str(i) + " " + str(j))
          print("Radio Difference: " + str(radioDifference))
          print("Constraint: " + str(constraintCheck))
        if radioDifference < constraintCheck:
          isValid = False
  
  return isValid

def generateRadioLabelingForLine(length):
  labeling = [-1] * length
  halfway = int(math.floor(length / 2))

  # Initialize the middle of the line to 1
  labeling[halfway - 1] = 1

  currentIndex = halfway - 1
  previousIndex = length - 1

  for i in range(math.ceil(length / 2)):
    previousIndex = currentIndex
    currentIndex = length - i - 1

    labeling[currentIndex] = labeling[previousIndex] + length - (currentIndex - previousIndex)
    
    previousIndex = currentIndex
    currentIndex = halfway - i - 2
    if currentIndex >= 0:
      labeling[currentIndex] = labeling[previousIndex] + length - (previousIndex - currentIndex)

  return labeling

#############
## Startup ##
#############

main()