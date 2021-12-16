#! /usr/bin/env python  

 
from lsystem import LSystems
import turtle
from tkinter import *

class App(Frame):
    def __init__(self, master):
      Frame.__init__(self, master)
      self.QUIT = Button(self)
      self.QUIT["text"] = "QUIT"
      self.QUIT["command"] =  self.quit
      self.QUIT.pack({"side": "left"})
      self.pack()
      
      turtle.setup(width=400,height=400)
      turtle.reset() 
      turtle.tracer(0)
      l=LSystems()
      
      
      self.setHilbert()
      
      path =l.iterate(self.axiom,self.rules,self.iterations)

      print("path:", path)
      l.draw(path,self.angle,self.forwardLength, self.draw)

    def setDragonCurve(self):
      self.axiom='FX'
      self.rules=[('X','X+YF+'), ('Y','-FX-Y')]
      self.draw='up'
      self.iterations=8
      self.angle=90
      self.forwardLength = 10
    
    def setCantorDust(self):
      self.axiom='F'
      self.rules=[('F','FfF'),('f','fff')]
      self.draw='up'
      self.iterations=8
      self.angle=90
      self.forwardLength = 10
    
    def setKoch(self):
      self.axiom='F'
      self.rules=[('F','F+F-F-F+F')]
      self.draw='left'
      self.iterations=5
      self.angle=90
      self.forwardLength = 10
      turtle.up()
      turtle.setx(100)
      turtle.down()
      
    def setPenrose(self):
      self.axiom = '[7]++[7]++[7]++[7]++[7]'
      self.rules = [('6', '8F++9F----7F[-8F----6F]++'), ('7', '+8F--9F[---6F--7F]+'), ('8', '-6F++7F[+++8F++9F]-'), ('9', '--8F++++6F[+9F++++7F]--7F'), ('F', '')]
      self.draw = 'up'
      self.iterations = 4
      self.angle = 36
      self.forwardLength = 10
      
        
    def setPlant(self):
      self.axiom='X'
      self.rules=[('X','F-[[X]+X]+F[+FX]-X'),('F','FF')]
      self.draw='up'
      self.iterations=6
      self.angle=25
      self.forwardLength=5
      turtle.up()
      turtle.sety(-300)
      turtle.down()
    
    def setSierpinski(self):
      self.axiom='AB'
      self.rules=[('A','B-A-B'),('B','A+B+A')]
      self.draw='up'
      self.iterations=6
      self.angle=60
      self.forwardLength=5
      turtle.up()
      turtle.sety(-300)
      #turtle.setx(-300)
      turtle.down()
      
    def setTree2(self):
      self.axiom = 'F'
      self.rules = [('F','FF+[+F-F-F]-[-F+F+F]')]
      self.draw = 'up'
      self.iterations = 6
      self.angle = 22
      self.forwardLength = 5
    
    def setHilbert(self):
      self.axiom = 'X'
      self.rules = [('F','F'),('X','-YF+XFX+FY-'),('Y','+XF-YFY-FX+')]
      self.draw = 'up'
      self.iterations = 1
      self.angle = 90
      self.forwardLength = 5
      
if __name__=="__main__":
  root = Tk()d
  app  = App(root)
  app.mainloop()