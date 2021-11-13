#############
## Imports ##
#############

import copy

################
## Graph Init ##
################

testGraph = [
  [2],
  [1, 3],
  [2, 4],
  [3]
]

proposedLabeling = [0, 0, 0, 0]

########################
## Method Declaration ##
########################

def main():
  if len(testGraph) != len(proposedLabeling):
    print("The labeling must contain an element for each vertex in the graph")
    return
  
  print ("Hello World")
  diameter = diameterOf(testGraph)
  print("Diameter is : " + str(diameter))

  for v in testGraph:
    for a in v:
      print(a, end=" ")
    print()

def diameterOf(graph):
  temp = copy.deepcopy(graph)
  
  temp[1][0] = 0

  for v in temp:
    for a in v:
      print(a, end=" ")
    print()
  # TODO: Calculate the diameter of testGraph
  return -1

#############
## Startup ##
#############

main()