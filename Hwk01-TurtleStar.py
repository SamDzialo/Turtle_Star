"""
file: Hwk01.py
author: Sam Dzialo
Email: sad8333@rit.edu
language: python3.7
description: Star turtle solution
"""
import turtle


def triangle():
    """draws an equilateral triangle facing what ever angle
    turtle is facing towards"""
    turtle.down()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)


def move():
    """moves turtle into a spot where the next triangle
    is meant to be made."""
    turtle.left(120)
    turtle.forward(100)
    turtle.right(72)


def star():
    """calls the triangle and move functions in order to create
    the desired star shape."""
    triangle()
    move()
    triangle()
    move()
    triangle()
    move()
    triangle()
    move()
    triangle()
    move()


star()
