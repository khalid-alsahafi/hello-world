from turtle import *
from time import sleep

#hideturtle()
tracer(1, 0.001)
speed(0)

def step(distance):
	up()
	fd(distance)
	down()

def tel(x, y):
	up()
	goto(x, y)
	down()
	
def square(size):
	for i in range(4):
			fd(size)
			lt(90)
		
def triangle(size):
	for i in range(3):
		fd(size)
		lt(360/3)
	
def rect(width, height):
	for i in range(4):
		fd(width)
		lt(90)
		fd(height)
		lt(90)
	
def grid(columns, rows, size):
    origin = pos()
    def box():
        fd(size)
        lt(90)
        fd(size)
        bk(size)
        rt(90)
    for i in range(rows):
        for l in range(columns):
            box()

        bk(size * columns)
        lt(90); fd(size); rt(90)
    tel(origin[0], origin[1])
    rect(columns * size, rows * size)

def coordinate(rows, columns, size):
	original_heading = heading()
	for i in range(4):
		width(4)
		if heading() == original_heading or heading() == original_heading + 180:
			fd(size * rows)
			stamp()
			bk(size * rows)
			width(1)
			grid(rows, columns, size)
		else:
			
			fd(size * columns)
			stamp()
			bk(size * columns)
			width(1)
			grid(columns, rows, size)
		lt(90)

def parallelogram(base, tilted_side, tilt_angle):
	fd(base)
	lt(tilt_angle)
	fd(tilted_side)
	rt(tilt_angle)
	bk(base)
	lt(tilt_angle)
	bk(tilted_side)
	rt(tilt_angle)


for i in range(360//2):
	square(i*2)
	lt(2)

	



done()
