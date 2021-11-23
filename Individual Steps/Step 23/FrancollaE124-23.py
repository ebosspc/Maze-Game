'''
PLTW Lesson 1.2.4
@authors: Ethan the Python Master
'''

#####-Imports-#####
#Import turtle library for drawing functions and display
import turtle as trtl

#Import random library to generate random values to be used later
import random as rand


#####-Game Config-#####
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

#####-Functions-#####
#Define a function to move the maze drawing turtle to the necessary location to start drawing a door
#Pass distance_before_door through as a parameter, since it will change everytime this function is called
def goto_door(distance_before_door):
    #Draw the wall up until the door
    maze_painter.pendown()
    maze_painter.forward(distance_before_door)

#Define a function to move the maze drawing turtle to the necessary location to start drawing a barrier
#Pass distance_before_barrier through as a parameter, since it will change everytime this function is called
def goto_barrier(distance_before_barrier):
    #Draw the wall up until the barrier
    maze_painter.pendown()
    maze_painter.forward(distance_before_barrier)

#Define a function to draw a barrier in the maze
def draw_barrier():
    #Draw a barrier segment off of the wall
    maze_painter.pendown()
    maze_painter.left(90)
    maze_painter.forward(barrier_length)
    maze_painter.back(barrier_length)
    maze_painter.right(90)

#Define a function to draw a door in the maze
def draw_door():
    #Draw a door in a wall via a temporary pen liftoff
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()

#Define a function to randomly generate the position of the door
#Pass wall_length through as a parameter, since it will change everytime this function is called
def generate_rand_door_distance(wall_length):
    #Allow the distance before door's variable to accessed in other places in the code
    global distance_before_door

    #Ensure random doors aren't drawn too close to the edge of a wall, creating visual errors
    distance_before_door = rand.randint(0, wall_length - door_width)

#Define a function to randomly generate the position of the door
#Pass wall_length through as a parameter, since it will change everytime this function is called
def generate_rand_barrier_distance(wall_length):
    #Allow the distance before barrier's variable to accessed in other places in the code
    global distance_before_barrier

    #Ensure random barriers aren't drawn too close to the edge of the wall
    distance_before_barrier = rand.randint(door_width, wall_length - door_width)


#####-Setup-#####
'''
Create a randomly generated maze in a for loop with a contorllable features
define by varibles in the Game Config Section.
Each time the program is run, a new randomly generated maze will be created.
Although checks are not built in to ensure the maze will be 100% solvable,
due to the way i is cosntructed there will typically always be at least one solution.
'''

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
            generate_rand_door_distance(wall_length)

            #Draw the wall up until the door
            goto_door(distance_before_door)

            #Draw the door
            draw_door()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_door - door_width)
    
    #Draw a wall with doors and barriers like normal
    else:
        #Generate random values for the placement of doors and barriers
        generate_rand_door_distance(wall_length)
        generate_rand_barrier_distance(wall_length)
    
        #Ensure barriers and doors can't render on top of each other by generating too close together
        while (abs(distance_before_door - distance_before_barrier) < door_width):
            #Generate random values for the positions of doors and barriers
            generate_rand_door_distance(wall_length)
            generate_rand_barrier_distance(wall_length)
        
        #Check to see if the door is supposed to be drawn before the barrier
        if (distance_before_door < distance_before_barrier):
            #Draw the wall up until the door
            goto_door(distance_before_door)

            #Draw the door
            draw_door()

            #Go to the starting location of the barrier
            maze_painter.forward(distance_before_barrier - door_width - distance_before_door)

            #Draw the barrier
            draw_barrier()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_barrier)
        
        #Check to see if the barrier shoudl be drawn before the door
        if (distance_before_door > distance_before_barrier):
            #Draw the wall up until the barrier
            goto_barrier(distance_before_barrier)

            #Draw the barrier
            draw_barrier()

            #Reset back to original position
            maze_painter.penup()
            maze_painter.back(distance_before_barrier)

            #Go to the door location
            goto_door(distance_before_door)

            #Draw the door
            draw_door()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_door - door_width)
        
    #Change direction and distance for next iteration
    maze_painter_new_heading = maze_painter_initial_heading + maze_painter_turning_angle * i 
    maze_painter.setheading(maze_painter_new_heading)
    maze_painter_extra_distance = maze_painter_extra_distance + extra_wall_length

#Hide the maze drawing turtle from view
maze_painter.hideturtle()


#####-Function Calls-#####
wn = trtl.Screen()
wn.mainloop()