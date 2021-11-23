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

#Define maze properties
number_of_walls = 25
extra_wall_length = 15
distance_before_door = 10
door_width = extra_wall_length * 2
barrier_length = extra_wall_length * 2
distance_before_barrier = 40
walls_before_doors = 1
walls_before_barriers = 8

#Define the maze creator's attributes
maze_painter_speed = 0
maze_painter_pencolor = "black"
maze_painter_fillcolor = "black"
maze_painter_initial_heading = 90
maze_painter_turning_angle = 90
maze_painter_initial_distance = 15
maze_painter_extra_distance = 0

#Give the maze creator turtle its defined attributes
maze_painter.speed(maze_painter_speed)
maze_painter.pencolor(maze_painter_pencolor)
maze_painter.fillcolor(maze_painter_fillcolor)
maze_painter.setheading(maze_painter_initial_heading)

#For loop to generate simple maze spiral with doors and walls
for i in range(number_of_walls):
    #To simplify the program create a variable that stores the total length of each wall
    wall_length = maze_painter_initial_distance + maze_painter_extra_distance

    #Check if the maze shouldn't be drawing doors or barriers at this point
    if (i < walls_before_doors or i < walls_before_barriers):
        #Check to ensure if no doors should be drawn
        if (i < walls_before_doors):
            #Draw a wall with no doors or barriers
            maze_painter.forward(wall_length)
        
        #Draw a wall with only a door
        else:
            #Generate a random value for the placement of the door
            distance_before_door = rand.randint(0, wall_length - door_width)

            #Draw the wall up until the door
            maze_painter.forward(distance_before_door)

            #Draw the door
            maze_painter.penup()
            maze_painter.forward(door_width)
            maze_painter.pendown()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_door - door_width)
    
    #Draw a wall with doors and barriers like normal
    else:
        #Generate random values for the placement of doors and barriers
        distance_before_door = rand.randint(0, wall_length - door_width)
        distance_before_barrier = rand.randint(door_width, wall_length - door_width)
    
        #Ensure barriers and doors can't render on top of each other by generating too close together
        while (abs(distance_before_door - distance_before_barrier) < door_width):
            #Generate random values for the positions of doors and barriers
            distance_before_door = rand.randint(0, wall_length - door_width)
            distance_before_barrier = rand.randint(door_width, wall_length - door_width)
        
        #Check to see if the door is supposed to be drawn before the barrier
        if (distance_before_door < distance_before_barrier):
            #Draw the wall up until the door
            maze_painter.pendown()
            maze_painter.forward(distance_before_door)

            #Draw the door
            maze_painter.penup()
            maze_painter.forward(door_width)
            maze_painter.pendown()

            #Draw the barrier after
            maze_painter.forward(distance_before_barrier-door_width-distance_before_door)
            maze_painter.pendown()
            maze_painter.left(90)
            maze_painter.forward(barrier_length)
            maze_painter.back(barrier_length)
            maze_painter.right(90)

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_barrier)
        
        #Check to see if the barrier shoudl be drawn before the door
        if (distance_before_door > distance_before_barrier):
            #Draw the wall up until the barrier
            maze_painter.forward(distance_before_barrier)

            #Draw the barrier
            maze_painter.left(90)
            maze_painter.forward(barrier_length)
            maze_painter.back(barrier_length)
            maze_painter.right(90)

            #Reset back to original position
            maze_painter.penup()
            maze_painter.back(distance_before_barrier)

            #Draw the door after
            maze_painter.pendown()
            maze_painter.forward(distance_before_door)
            maze_painter.penup()
            maze_painter.forward(door_width)
            maze_painter.pendown()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_door - door_width)
        
    #Change direction and distance for next iteration
    maze_painter_new_heading = maze_painter_initial_heading + maze_painter_turning_angle * i 
    maze_painter.setheading(maze_painter_new_heading)
    maze_painter_extra_distance = maze_painter_extra_distance + extra_wall_length

#Hide the maze drawing turtle from view
maze_painter.hideturtle()


#####-Game Config-#####


#####-Functions-#####


#####-Function Calls-#####
wn = trtl.Screen()
wn.mainloop()
