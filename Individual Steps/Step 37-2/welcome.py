'''
PLTW Lesson 1.2.4
@authors: Ethan Francolla, Kaelin Conklin
'''

#####-Imports-#####
#Import turtle library for drawing functions and display
import turtle as trtl

#Import random library to generate random values to be used later
import random as rand

#Define this variable as an integer. It doesn't really matter what it is as long as it isn't 1 or 0
instructions_request = 2

global continue_with_loop
#Define a variable that will either continue or break the following while loop
continue_with_loop = 1

#Define a variable to determine whether or not a user is in developer mode
developer_mode = 0

#####-Functions-#####
def welcome_user():
    #Create a message in the terminal instructing users how to use the program
    print("-----Welcome to the game!-----\nWould you like to read the instructions for the game?")

def print_instructions():
    #Explain to users how the game work
    print("\n-Game Info-")
    print("This game will generate a randomly constructed filled with doors and barriers.")
    print("doors are blank spaces or gaps in the wall that you can guide the maze navigator through.")
    print("Eventually, if you work your way through enough doors you will reach the outside of the maze and complete the game!")
    print("Barriers are obstructions you will find in your path, seeming like parts of the wall jutting out.")
    print("To complete your objective, you will have to go through doors in the maze while avoiding barrier obstructions.")
    print("The objective of the game is to use your keyboard to control a maze navigator and guide it out of the maze.")

    #Describe the game controls
    print("Below you will find a list of controls for the maze navigator.")
    print("\n-Controls-")
    print("Up Arrow: Turn up and go up")
    print("Right Arrow: Turn right and go right")
    print("Down Arrow: Turn down and go down")
    print("Left Arrow: Turn left and go left")
    print("G: Go forward in the direction the navigator is pointed")
    print("O: Increase the speed of the navigator")
    print("L: Decrease the speed of the navigator")
    print("P: Terminate the game")