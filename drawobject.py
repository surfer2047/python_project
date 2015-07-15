#!/usr/bin/env python

import turtle

window = turtle.Screen()
window.bgcolor("green")
shape = turtle.Turtle()

def draw_square():
	for i in range(0,4):
		shape.forward(100)
		shape.right(90)

draw_square()
shape.circle(100)
window.exitonclick()

