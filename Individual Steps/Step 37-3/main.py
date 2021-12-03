'''
PLTW Lesson 1.2.4
@authors: Ethan Francolla, Kaelin Conklin
'''

#####-Imports-#####
#Import turtle library for drawing functions and display
import turtle as trtl

#Import random library to generate random values to be used later
import random as rand

#Import library that contains functions necessary to begin the program
import welcome as welcome


#####-Game Info-#####
#Define this variable as an integer. It doesn't really matter what it is as long as it isn't 1 or 0
instructions_request = 2

#Define a variable that will either continue or break the following while loop
continue_with_loop = 1

#Define a variable to determine whether or not a user is in developer mode
developer_mode = 0

#Welcome the user, give instructions if requested, and give developer perms
welcome.welcome_user()

#Ask the user if they want instructions until they enter a valid input
while (continue_with_loop == 1):
    #Store the user input in a variable
    instructions_request = str(input("Please write y for yes, n for no, and d for developer mode: "))

    #Check if the user selected yes and adjust variables appropriately
    if instructions_request == "y":
        instructions_request = 1
        continue_with_loop = 0

    #Check if the user selected no and adjust variables appropriately
    elif instructions_request == "n":
        instructions_request = 0
        continue_with_loop = 0
        
    elif instructions_request == "d":
        developer_mode = 1
        continue_with_loop = 1

        #Print a message to inform a user that they are in developer mode
        print("You are now in developer mode.")
        
    #Output an error message if the user enters an invalid input
    else:
        print("Sorry! That was not a valid input.\nPlease try again.")

#Print the instructions if the user wants them
if instructions_request == 1:
    #Print the instructions
    welcome.print_instructions()

#Don't print the instructions if the user doesn't want them
elif instructions_request == 0:
    print("Welcome back!")

#Inform the user the game is starting
print("Lets start the game!")

#Inform the user if they are running the program as a developer
if developer_mode == 1:
    print("You are running this program as a developer.")

#####-Game Config-#####
#Define an empty list that will be used to store all of the turtles in one place
master_turtles_list = []

#Generate a screen for the game to diplay on
wn = trtl.Screen()

#Create turtle to generate the simple maze and define its initial attributes and add it to the main turtles list
maze_painter = trtl.Turtle()
master_turtles_list.append(maze_painter)

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Maze Painter Turtle Created")

#Create turtle which will act as the "maze runner", which the user can control to guide it through the maze and add it to the main turtles list
maze_navigator = trtl.Turtle()
master_turtles_list.append(maze_navigator)

#Output a message for debugging if the user is in developer mode
if developer_mode == 1:
    print("Maze Navigator Turtle Created")

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

#Define the maze navigator's attributes
maze_navigator_x_moving_distance = 2
maze_navigator_y_moving_distance = 2
maze_navigator_forward_moving_distance = 2
maze_navigator_fillcolor = "blue"
maze_navigator_shape = "triangle"
maze_navigator_shapesize = 0.5
maze_navigator_pencolor = "blue"
maze_navigator_speed = 0
maze_navigator_initial_x_position = -(maze_painter_initial_distance)
maze_navigator_initial_y_position = maze_painter_initial_distance

#Give the maze creator turtle its defined attributes
maze_painter.speed(maze_painter_speed)
maze_painter.pencolor(maze_painter_pencolor)
maze_painter.fillcolor(maze_painter_fillcolor)
maze_painter.setheading(maze_painter_initial_heading)

#Give the maze navigator turtle its defined attributes
maze_navigator.penup()
maze_navigator.goto(maze_navigator_initial_x_position, maze_navigator_initial_y_position)
maze_navigator.fillcolor(maze_navigator_fillcolor)
maze_navigator.pencolor(maze_navigator_pencolor)
maze_navigator.shape(maze_navigator_shape)
maze_navigator.shapesize(maze_navigator_shapesize)
maze_navigator.speed(maze_navigator_speed)

#####-Functions-#####
#Define a function to move the maze drawing turtle to the necessary location to start drawing a door
#Pass distance_before_door through as a parameter, since it will change everytime this function is called
def goto_door(distance_before_door):
    #Draw the wall up until the door
    maze_painter.pendown()
    maze_painter.forward(distance_before_door)

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Went to Door")

#Define a function to move the maze drawing turtle to the necessary location to start drawing a barrier
#Pass distance_before_barrier through as a parameter, since it will change everytime this function is called
def goto_barrier(distance_before_barrier):
    #Draw the wall up until the barrier
    maze_painter.pendown()
    maze_painter.forward(distance_before_barrier)

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Went to Barrier")

#Define a function to draw a barrier in the maze
def draw_barrier():
    #Draw a barrier segment off of the wall
    maze_painter.pendown()
    maze_painter.left(90)
    maze_painter.forward(barrier_length)
    maze_painter.back(barrier_length)
    maze_painter.right(90)

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Drew Barrier")

#Define a function to draw a door in the maze
def draw_door():
    #Draw a door in a wall via a temporary pen liftoff
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Drew Door")

#Define a function to randomly generate the position of the door
#Pass wall_length through as a parameter, since it will change everytime this function is called
def generate_rand_door_distance(wall_length):
    #Allow the distance before door's variable to accessed in other places in the code
    global distance_before_door

    #Ensure random doors aren't drawn too close to the edge of a wall, creating visual errors
    distance_before_door = rand.randint(0, wall_length - door_width)

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Generated Random Door Distance")

#Define a function to randomly generate the position of the door
#Pass wall_length through as a parameter, since it will change everytime this function is called
def generate_rand_barrier_distance(wall_length):
    #Allow the distance before barrier's variable to accessed in other places in the code
    global distance_before_barrier

    #Ensure random barriers aren't drawn too close to the edge of the wall
    distance_before_barrier = rand.randint(door_width, wall_length - door_width)

    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Generated Random Barrier Distance")

#Define a function to terminate the program when the user desires
def terminate_program():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Terminating program...")
    
    #Clear all turtles, drawing, and images present on the screen
    for i in range(len(master_turtles_list)):
        #Clear the turtles and their traces
        master_turtles_list[i].clear()
        master_turtles_list[i].hideturtle()

    #Output message informing the user they terminated the program
    print("You have successfully terminated the program.\nThanks for playing!")

def restart_game():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Restarting game...")
    
    #Clear all traces of the maze navigator turtle
    maze_navigator.clear()
    maze_navigator.hideturtle()
    maze_navigator.penup()

    #Reset the maze navigator turtle back to its origianl position
    maze_navigator.goto(maze_navigator_initial_x_position, maze_navigator_initial_y_position)

    #Reveal the maze navigator turtle in its new position
    maze_navigator.showturtle()
    maze_navigator.pendown()

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def up_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Up Arrow pressed")

    #Turn the maze navigator up and move it forward
    maze_navigator.pendown()
    maze_navigator.setheading(90)
    maze_navigator.goto(maze_navigator.xcor(), maze_navigator.ycor() + maze_navigator_y_moving_distance)

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def down_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Down Arrow pressed")

    #Turn the maze navigator down and move it forward
    maze_navigator.pendown()
    maze_navigator.setheading(270)
    maze_navigator.goto(maze_navigator.xcor(), maze_navigator.ycor() - maze_navigator_y_moving_distance)

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def left_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Left Arrow pressed")

    #Turn the maze navigator left and move it forward
    maze_navigator.pendown()
    maze_navigator.setheading(180)
    maze_navigator.goto(maze_navigator.xcor() - maze_navigator_x_moving_distance, maze_navigator.ycor())

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def right_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Right Arrow pressed")

    #Turn the maze navigator right and move it forward
    maze_navigator.pendown()
    maze_navigator.setheading(0)
    maze_navigator.goto(maze_navigator.xcor() + maze_navigator_x_moving_distance, maze_navigator.ycor())

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def g_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("G pressed")
    
    #Move the maze navigator forward
    maze_navigator.pendown()
    maze_navigator.forward(maze_navigator_forward_moving_distance)

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def o_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("O pressed")
    
    #Allow these variable to be accessed in other functions
    global maze_navigator_x_moving_distance, maze_navigator_y_moving_distance

    #Increase the distance that the maze navigator will travel each time a function is called to move it, essentially increasing its "speed"
    maze_navigator_x_moving_distance = maze_navigator_x_moving_distance + 1
    maze_navigator_y_moving_distance = maze_navigator_y_moving_distance + 1

    #Print a statement for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Maze Runner x and y moving distance increased by 1. It is now:", maze_navigator_x_moving_distance)

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def l_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("L pressed")

    #Allow these variable to be accessed in other functions
    global maze_navigator_x_moving_distance, maze_navigator_y_moving_distance 

    #Decrease the distance that the maze navigator will travel each time a function is called to move it, essentially decreasing its "speed"
    maze_navigator_x_moving_distance = maze_navigator_x_moving_distance - 1
    maze_navigator_y_moving_distance = maze_navigator_y_moving_distance - 1

    #Print a statement for debugging if the user is in developer mode
    if developer_mode == 1:
        print("Maze Runner x and y moving distace decreased by 1. It is now:", maze_navigator_x_moving_distance)

#Define a function to execute a specified action below if a user presses a certain key on their keyboard
def p_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("P pressed")
    
    #Terminate the program
    terminate_program()

def i_pressed():
    #Output a message for debugging if the user is in developer mode
    if developer_mode == 1:
        print("I pressed")
    
    #Restart the game
    restart_game()


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

            #Output a message for debugging if the user is in developer mode
            if developer_mode == 1:
                print("Drew Rest of Wall")
    
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

            #Output a message for debugging if the user is in developer mode
            if developer_mode == 1:
                print("Went to Barrier")

            #Draw the barrier
            draw_barrier()

            #Draw the rest of the wall
            maze_painter.forward(wall_length - distance_before_barrier)

            #Output a message for debugging if the user is in developer mode
            if developer_mode == 1:
                print("Drew Rest of Wall")
        
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

            #Output a message for debugging if the user is in developer mode
            if developer_mode == 1:
                print("Drew Rest of Wall")
        
    #Change direction and distance for next iteration
    maze_painter_new_heading = maze_painter_initial_heading + maze_painter_turning_angle * i 
    maze_painter.setheading(maze_painter_new_heading)
    maze_painter_extra_distance = maze_painter_extra_distance + extra_wall_length

#Hide the maze drawing turtle from view
maze_painter.hideturtle()


#####-Function Calls-#####
#Execute the function below if the specified key is pressed
wn.onkeypress(up_pressed, "Up")

#Execute the function below if the specified key is pressed
wn.onkeypress(down_pressed, "Down")

#Execute the function below if the specified key is pressed
wn.onkeypress(left_pressed, "Left")

#Execute the function below if the specified key is pressed
wn.onkeypress(right_pressed, "Right")

#Execute the function below if the specified key is pressed
wn.onkeypress(g_pressed, "g")

#Execute the function below if the specified key is pressed
wn.onkeypress(o_pressed, "o")

#Execute the function below if the specified key is pressed
wn.onkeypress(l_pressed, "l")

#Execute the function below if the specified key is pressed
wn.onkeypress(p_pressed, "p")

#Execute the function below if the specified key is pressed
wn.onkeypress(i_pressed, "i")

#Listen for the user's key presses to control the game
wn.listen()

#Keep the display running and persistent
wn.mainloop()