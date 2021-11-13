#############
## Imports ##
#############

import copy
import math
import numpy

################
## Graph Init ##
################

testGraph = [
  [1],
  [0, 2],
  [1, 3],
  [2]
]

proposedLabeling = [0, 0, 0, 0]

########################
## Method Declaration ##
########################

def main():
  if len(testGraph) != len(proposedLabeling):
    print("The labeling must contain an element for each vertex in the graph")
    return
  
  distance = distanceMatrix(testGraph)
  print("Distance Matrix")
  printGraph(distance)

  diameter = numpy.amax(distance)
  print("Diameter of testGraph")
  print(int(diameter))

# Floyd's Algorithm
# Return a 2D array
def distanceMatrix(graph):
  # Initialize to infinity
  distance = []
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

#############
## Startup ##
#############

main()