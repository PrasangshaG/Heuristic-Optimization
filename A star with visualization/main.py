import RandGraph
import DrawGrid
import numpy
from numpy import *
import heapq
import Astar



# Generate the random graph with % of obstable grids cannot be visited
n_Row, n_Col, start, end, Cells, Blocked_nodes = RandGraph.GridGenerator()

graphu = [([1] * n_Row) for row in range(n_Row) ]

for blocknode in Blocked_nodes:
  xc = blocknode[0]
  yc = blocknode[1]
  graphu[xc][yc] = 0

#print(graphu)

cost = 1
route = Astar.astar(graphu, cost, start, end)
print(route)
 


'''
Output of Grid.Generator() function
n_Row: number of rows
n_Col: number of columns
start: starting grid
end: destination grid
Cells: entire list of grids, with 'x,x' represents cannot be visited
Blocked_grid: list of grids that cannot be visited

'''
# soultion route example
# route = [(1,1), (1,2), (2,3), (3,4), (4,5)]
# Ideally the solution of Astar can be in a structure of a list of grids
# Then code will draw the route in the graph as well  

# Draw the grid graph
DrawGrid.Grid_Graph(n_Row, n_Col, Cells, route)  









