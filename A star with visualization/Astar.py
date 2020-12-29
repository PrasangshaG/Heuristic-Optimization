import numpy
from numpy import *
import heapq

class Cell:
    def __init__(self, prev=None, loc = None):
        self.prev = prev
        self.loc = loc
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.loc == other.loc
    
    def __repr__(self):
        return f"{self.loc} - g: {self.g} h: {self.h} f: {self.f}"
    
    def __lt__(self, other):
      return self.f < other.f
    
    def __gt__(self, other):
      return self.f > other.f


def findpath(cell, graph):
    path = []
    current = cell
    while current is not None:
        path.append(current.loc)
        current = current.prev
    return path[::-1]


def astar(graph, cost, start, end):
    startcell = Cell(None, start)
    startcell.g = 0
    startcell.h = 0
    startcell.f = 0
    
    endcell = Cell(None, end)
    endcell.g = 0
    endcell.h = 0
    endcell.f = 0

    openlist = []
    closedlist = []
    
    heapq.heapify(openlist) 
    heapq.heappush(openlist, startcell)
    
    ite = 0
    maxite = 10000
    
    allowed_moves = ((0, -1), (0, 1), (-1, 0), (1, 0) , (-1, -1), (-1, 1), (1, -1), (1, 1),)
    
    maxrows, maxcols = numpy.shape(graph)
    
    while len(openlist) > 0:
        
        ite = ite+1
        if(ite > maxite):
            print("can't find destination")
            return findpath(currentcell, graph)
        
        currentcell = heapq.heappop(openlist)

        closedlist.append(currentcell)
         
        if currentcell == endcell:
            return findpath(currentcell, graph)

        
        successors = []

        for move in allowed_moves:
            cell_loc = (currentcell.loc[0] + move[0], currentcell.loc[1] + move[1])
            
            if(cell_loc[0] > (maxrows-1) or cell_loc[0] < 0 or cell_loc[1] > (maxcols-1) or cell_loc[1] < 0):
                continue
            
            if graph[cell_loc[0]][cell_loc[1]] != 1:
                continue
            
            new_cell = Cell(currentcell, cell_loc)
            successors.append(new_cell)    
        
        for successor in successors:
            if len([closedcell for closedcell in closedlist if closedcell == successor]) > 0:
                continue
            successor.g = currentcell.g + cost
            successor.h = (pow((successor.loc[0] - endcell.loc[0]),2) + pow((successor.loc[1] - endcell.loc[1]),2))
            successor.f = successor.g + successor.h

            if len([openn for openn in openlist if successor.loc == openn.loc and successor.g > openn.g]) > 0:
                continue
                
            heapq.heappush(openlist, successor)



