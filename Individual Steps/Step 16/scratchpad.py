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
true_distance_before_barrier = 40
distance_before_barrier = 40
walls_before_doors = 3
walls_before_barriers = 7

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
    #To simplify the program create a variable that stores the length of each wall
    wall_length = maze_painter_initial_distance + maze_painter_extra_distance

    #Don't draw a door on the first iteration to avoid maze overlap
    if i < walls_before_doors:
        #Don't account for walls or barriers if they aren't being drawn
        distance_before_barrier = 0
        distance_before_door = 0
        #Draw the first wall normally
        maze_painter.forward(wall_length)

    #Draw a door in each wall after the first iteration
    else:
        #Generate random values for the distance from the start of the wall to barrriers and doors
        distance_before_door = rand.randint(door_width, wall_length - door_width)
        distance_before_barrier = rand.randint(door_width, wall_length - door_width)

        #Ensure the barriers and doors don't overlap by continuously picking random variables until they are spread out enough
        while (abs(distance_before_door - distance_before_barrier) < door_width):
            #Generate random values for the distance from the start of the wall to barrriers and doors
            distance_before_door = rand.randint(0, wall_length - door_width)
            distance_before_barrier = rand.randint(door_width, wall_length - door_width)
        
        #Only start drawing barriers after a certain point to avoid overlap
        if i < walls_before_barriers:
            #Don't account for barrier length when they aren't being drawn yet
            distance_before_barrier = 0

            #Only draw walls with doors
            maze_painter.forward(distance_before_door)
            maze_painter.penup()
            maze_painter.forward(door_width)
            maze_painter.pendown()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_door - door_width)

        else:
            #Check if the door will be drawn before the barrier
            if distance_before_door < distance_before_barrier:
                #Find the distance between the barrier and the door left to draw
                distance_between_door_and_barrier = distance_before_barrier - distance_before_door

                #Draw the door first
                maze_painter.forward(distance_before_door)
                maze_painter.penup()
                maze_painter.forward(door_width)
                maze_painter.pendown()

                #Draw the barrier second
                maze_painter.forward(distance_between_door_and_barrier)
                maze_painter.left(90)
                maze_painter.forward(barrier_length)
                maze_painter.back(barrier_length)
                maze_painter.right(90)

                #Draw the rest of the wall
                maze_painter.forward(wall_length - distance_before_door - door_width - distance_between_door_and_barrier)
            
            #Check if the barrier will be drawn before the door
            if distance_before_door > distance_before_barrier:
                #Find the distance between the barrier and the door left to draw
                distance_between_door_and_barrier = distance_before_door - distance_before_barrier

                #Draw the barrier first
                maze_painter.forward(distance_before_barrier)
                maze_painter.left(90)
                maze_painter.forward(barrier_length)
                maze_painter.back(barrier_length)
                maze_painter.right(90)

                #Draw the door second
                maze_painter.forward(distance_between_door_and_barrier)
                maze_painter.penup()
                maze_painter.forward(door_width)
                maze_painter.pendown()

                #Draw the rest of the wall
                maze_painter.forward(wall_length - distance_before_barrier - door_width - distance_between_door_and_barrier)
    
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