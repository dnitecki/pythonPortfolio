# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:58:00 2019

@author: dominick nitecki
"""

import random
from turtle import *
from tkinter import *

def EndGame():
    msg = Message(None, text=f'Congrats player {turn}, you won!', width=700, font=('times',40))
    msg.pack()
    mainloop()

def TieGame():
    msg = Message(None, text='Game over, it is a tie!', width=700, font=('times',40))
    msg.pack()
    mainloop()    
    
setup(700,600, 10, 70)
hideturtle()
bgcolor("light green")

pensize(5)
for i in range(-250,350,100):  
    up()
    goto(i, -350)
    down()
    goto(i, 350)
    up()
    
pensize(1)
pencolor("grey")
for i in range(-200,300,100):  
    up()
    goto(-350,i)
    down()
    goto(350,i)
    up()

col=1
for x in range(-300, 350, 100):
    goto(x,270)
    write(col,font=('Arial',20,'normal'))
    col += 1
update()

validinputs=[1,2,3,4,5,6,7]
xs=[x for x in range(-300, 350, 100)]
ys=[y for y in range(-250,300,100)]
col=[list(),list(),list(),list(),list(),list(),list()]

turn="red"

def WinGame(inp,turn):
    complete=False
    x=inp-1
    y=len(col[x])
    try:
        if col[x-1][y]==turn and col[x+2][y]==turn and col[x+1][y]==turn and x>=1:
                complete=True          
    except IndexError:pass
    try:
        if col[x-1][y]==turn and col[x-2][y]==turn and col[x+1][y]==turn and x>=2:
                complete=True            
    except IndexError:pass

    try:
        if col[x-1][y]==turn and col[x-2][y]==turn and col[x-3][y]==turn and x>=3:
                complete=True            
    except IndexError:pass
    try:
        if col[x][y-1]==turn and col[x][y-2]==turn and col[x][y-3]==turn and y>=3:
                complete=True     
    except IndexError:pass

    try:
        if col[x+1][y]==turn and col[x+2][y]==turn and col[x+3][y]==turn:
                complete=True        
    except IndexError:pass
    try:
        if col[x+1][y-1]==turn and col[x+2][y-2]==turn and col[x+3][y-3]==turn and y>=3:
                complete=True         
    except IndexError:pass
    try:
        if col[x-1][y+1]==turn and col[x+1][y-1]==turn and col[x+2][y-2]==turn and x>=1 and y>=2:
                complete=True      
    except IndexError:pass
    try:
        if col[x-1][y+1]==turn and col[x-2][y+2]==turn and col[x+1][y-1]==turn and x>=1 and y>=1:
                complete=True      
    except IndexError:pass

    try:
        if col[x-1][y+1]==turn and col[x-2][y+2]==turn and col[x-3][y+3]==turn  and x>=3:
                complete=True        
    except IndexError:pass

    try:
        if col[x+1][y+1]==turn and col[x+2][y+2]==turn and col[x+3][y+3]==turn:
                complete=True       
    except IndexError:pass
    try:
        if col[x-1][y-1]==turn and col[x+1][y+1]==turn and col[x+2][y+2]==turn  and x>=1 and y>=1:
                complete=True      
    except IndexError:pass
    try:     
        if col[x-1][y-1]==turn and col[x-2][y-2]==turn and col[x+1][y+1]==turn  and x>=2 and y>=2:
                complete=True
    except IndexError:pass
    try:
        if col[x-1][y-1]==turn and col[x-2][y-2]==turn and col[x-3][y-3]==turn  and x>=3 and y>=3:
                complete=True      
    except IndexError:pass

    return complete

for i in range(21):
    inp=int(input(f"What's your move, player {turn}?"))
    if inp not in validinputs:
        while True:
            inp=int(input(f"Please reenter a valid move, player {turn}?"))
            if inp in validinputs:break
    up()
    goto(xs[inp-1],ys[len(col[inp-1])])
    dot(80,turn)
   
    if WinGame(inp,turn)==True:
        EndGame()
        break
    col[inp-1].append(turn)
    if len(col[inp-1])==6:validinputs.remove(inp)
    if turn=="red":turn="yellow"
    else:turn="red"               

    inp=random.choice(validinputs)
    print(f"The computer, who is also player {turn}, chooses {inp}.")
    up()
    goto(xs[inp-1],ys[len(col[inp-1])])
    dot(80,turn)
   
    if WinGame(inp,turn)==True:
        EndGame()
        break
    if i==20:TieGame()
    col[inp-1].append(turn)
    if len(col[inp-1])==6:validinputs.remove(inp)
    if turn=="red":turn="yellow"
    else:turn="red"            