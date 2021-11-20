'''
PLTW Lesson 1.2.4
@authors: Ethan Francolla
'''

#####-Imports-#####
#Import turtle library for drawing functions and display
import turtle as trtl

#Import random library to generate random values to be used later
import random as rand


#####-Setup-#####
#Create turtle to generate the simple maze and define its initial attributes
maze_painter = trtl.Turtle()

#Define wall properties
number_of_walls = 25
extra_wall_length = 15
distance_before_door = 10
door_width = extra_wall_length * 2

#Define the maze creator's attributes
maze_painter_speed = 0
maze_painter_pencolor = "black"
maze_painter_fillcolor = "black"
maze_painter_initial_heading = 90
maze_painter_initial_distance = 15
maze_painter_extra_distance = 0

#Give the maze creator turtle its defined attributes
maze_painter.speed(maze_painter_speed)
maze_painter.pencolor(maze_painter_pencolor)
maze_painter.fillcolor(maze_painter_fillcolor)
maze_painter.setheading(maze_painter_initial_heading)

#For loop to generate simple maze spiral with 25 walls according to the given picture
for i in range(number_of_walls):
    #Don't draw a door on the first iteration to avoid maze overlap
    if i > 0: #Will only not run on first iteration of for loop
        #Draw a door opening 10 pixels after each turn
        maze_painter.forward(distance_before_door)
        maze_painter.penup()
        maze_painter.forward(door_width)
        maze_painter.pendown()

    #Move the painter forward, leaving behind a trail
    maze_painter.forward(maze_painter_initial_distance + maze_painter_extra_distance - distance_before_door) 
    
    #Change direction and distance for next iteration
    maze_painter_new_heading = maze_painter_initial_heading + 90 * i 
    maze_painter.setheading(maze_painter_new_heading)
    maze_painter_extra_distance = maze_painter_extra_distance + extra_wall_length

#Hide the maze drawing turtle from view
maze_painter.hideturtle()


#####-Game Config-#####


#####-Functions-#####


#####-Function Calls-#####
wn = trtl.Screen()
wn.mainloop()