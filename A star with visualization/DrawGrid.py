from graphics import *

def Grid_Graph(n_Row, n_Col, Cells, route):
  # width, height = pyautogui.size()
  width = 600
  height = 600
  win = GraphWin("Grid_Graph", width, height)
  win.setCoords(0.0, 0.0, n_Col, n_Row)
  win.setBackground("yellow")

  # draw grid and the obstacles
  for y in range(n_Row):
    for x in range(n_Col):
      # draw grid line
      GridRow = Line(Point(0,y), Point(n_Col,y))
      GridCol = Line(Point(x,0), Point(x,n_Row))
      GridRow.draw(win)
      GridCol.draw(win)
      # draw blocked cells
      if Cells[y][x]== 'x,x':
        square = Rectangle(Point(x,y), Point(x+1,y+1))
        square.draw(win)
        square.setFill("gray")
      # text lable of the cells
      message = Text(Point(x+0.5,y+0.5), (str(y)+','+str(x)))
      message.draw(win)
      message.setSize(int(100/max(n_Row, n_Col)))

  # draw the solution route
  for i in range(n_Row):
    for j in range(n_Col):
      for node in route:
        if node[0] == i and node[1] == j:
          if node == route[0] or node == route[-1]:
            square = Rectangle(Point(j,i), Point(j+1,i+1))
            square.draw(win)
            square.setFill("green")
          else: 
            square = Rectangle(Point(j,i), Point(j+1,i+1))
            square.draw(win)
            square.setFill("red")

          route_text = Text(Point(j+0.5,i+0.5), (str(i)+','+str(j)))
          route_text.draw(win)
          route_text.setSize(int(100/max(n_Row, n_Col)))

  win.getMouse()
  win.close()











  