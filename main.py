'''
Code for Albania 2020
Assignment 1: Tic Tac Toe (Drawing)
Due: 2 August 2020
Name: Vigen Myrtolli

Overview: Draw a 3x3 grid and add 4 shapes (two stars and two diamonds)
as though you are playing Tic Tac Toe. See assignment handout for more
details. As a challenge, you may draw the Albanian Flag using turtle
and include your code (commented out) below.
'''
import turtle

turtle = turtle.Turtle()

turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(150)
turtle.penup()

#FirstStar
turtle.goto(5,-20)
turtle.pendown()

turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.penup()



#SecondStar
turtle.goto(55, -20)
turtle.pendown()

turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)
turtle.forward(40)
turtle.right(144)

turtle.penup();


#FirstDiamond
turtle.goto(5,-75)
turtle.pendown();

turtle.right(45)
turtle.pendown();

turtle.forward(30)


turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(45)
turtle.penup()

turtle.goto(5,-70)
turtle.penup();

#SecondDiamond
turtle.forward(55)
turtle.pendown();

turtle.left(90)
turtle.right(45)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.left(45)