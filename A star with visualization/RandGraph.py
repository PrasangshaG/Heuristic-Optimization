import random
import csv
# from datetime import date

def GridGenerator():
  n_Row, n_Col = input('Grid Size: number of Rows and number of Columns \n').split()
  n_Row = int(n_Row)
  n_Col = int(n_Col)

  start_point = input('Please input the starting grid without parentheses\n')
  end_point = input('Please input the destination grid without parentheses \n')
  start_point = tuple(map(int, start_point.split(',')))
  end_point = tuple(map(int, end_point.split(',')))

  filename = 'Grid'+"_"+str(n_Row)+'x'+str(n_Col)+'.csv'
  Grid_file = open(filename, "w", newline='')
  Grid_writer = csv.writer(Grid_file)
  Grid_writer.writerow([n_Row, n_Col])
  
  Cells = []
  Blocked_nodes = []
  Per_Blocked = int(input('Grid Parameter: Percentage of grids that cannot be visited \n'))
  for i in range(n_Row):
    GridRow = []
    for j in range(n_Col):
      if (i,j) == start_point or (i,j) == end_point:
        Gridstr = ','.join([str(i), str(j)])
        GridRow.append(Gridstr)
      else: 
        random_num = random.randrange(1, 100,)
        if random_num >= Per_Blocked:
          Gridstr = ','.join([str(i), str(j)])
          GridRow.append(Gridstr)
        else:
          GridRow.append('x,x')
          Blocked_nodes.append((i,j))
    Grid_writer.writerow(GridRow)
    Cells.append(GridRow)
  Grid_file.close()

  return n_Row, n_Col, start_point, end_point, Cells, Blocked_nodes






