#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
License:
Copyright (c) 2007, Kerim Mansour
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation 
      and/or other materials provided with the distribution.
    * Neither the name of the author nor the names of other contributors 
      may be used to endorse or promote products derived from this software without 
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, 
OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import turtle
class LSystems():
  """
  def __init__(self,rules=None, axiom=None):
    self.rules=rules #(Array of old/new)
    self.axiom=axiom
  """
  """
  Drawing methods below specific to turtle graphics. 
  You might just use the calculate methods if you dont want to use turtle
  """ 
  def draw(self, path, angle,length, dir='up'):
    if dir=='up':
      turtle.left(90)
    if dir=='down':
      turtle.right(90)
    if dir=='left':
      turtle.left(180)
    
    stack=list()
    methodToCall = {'F':lambda:self.drawForward(length),
                    'A':lambda:self.drawForward(length),
                    'B':lambda:self.drawForward(length),
                    'f':lambda:self.nonDrawForward(length),
                    '-':lambda:self.turn(angle,False),
                    '+':lambda:self.turn(angle),
                    '|':lambda:self.turn(180),
                    '[':lambda:stack.append(self.getState()),
                    ']':lambda:self.setState(stack.pop())
                    }
    for char in path:
      try:
        methodToCall[char]()
      except:
        pass#print 'char with no mapped action:',char
  
  def getState(self):
    return [turtle.heading(),turtle.position()]
  
  def setState(self,state):
    turtle.up() #cant we avoid that up and down here ?
    turtle.setheading(state[0])
    turtle.setx(state[1][0])
    turtle.sety(state[1][1])
    turtle.down()
    
  def drawForward(self,length):
    turtle.down()
    turtle.forward(length)
  
  def nonDrawForward(self,length):
    turtle.up()
    turtle.forward(length)
  
  def turn(self,angle,right=True):
    if right:
      turtle.right(angle)
    else:
      turtle.left(angle)
  """
  Drawing methods above specific to turtle graphics. 
  You might just use the calculate methods if you dont want to use turtle
  """       
  
  """
  iterates for "repetitions"-time over the axiom applying the rules 
  and using the result as new axiom in the next iteration
  """
  def iterate(self,axiom=None, rules=None, repetitions=1):
    if axiom==None or rules==None:
      return
    for repeat in range(0,repetitions):
      newpath=""
      i=0
      while i<len(axiom):
        found=False
        for old,new in rules:
          if old==axiom[i:i+len(old)]:
            newpath+=new
            i+=len(old)
            found=True
            continue          
        if not found:
          newpath+=axiom[i:i+1]
          i+=1
      axiom=newpath

    return axiom
      