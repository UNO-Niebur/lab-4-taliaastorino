#TurtleGraphics.py
#Name: Talia Astorino
#Date: 02/15/2026
#Purpose: Using turtle graphics commands, algorithms with loops, and writing reusable functions.

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS
def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    #Draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
def squaresInSquares(myTurtle, num):
    size = 200
    
    for i in range(num):
        drawSquare(myTurtle, size)
        
        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.pendown()
        
        size -= 20
def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(5)
    
    squaresInSquares(myTurtle, 5)
    
    myTurtle.penup()
    myTurtle.goto(-125, -100)
    myTurtle.pendown()
    
    fillCorner(myTurtle, 2)

    myTurtle.penup()
    myTurtle.goto(-125, 100)
    myTurtle.pendown()
    
    drawPolygon(myTurtle, 6)
    
    turtle.done()

main()
