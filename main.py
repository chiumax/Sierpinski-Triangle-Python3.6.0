#!/usr/bin/env python3
'''
Sierpinski's Triangle by dumblole

This is a recursive program that draws Sierpinski's triangle based off of
a couple of factors:
How many degrees does user want to see (iterations)
Does user want to see the drawing process
How long should one of the sides of the base triangle be
Color of the triangle
'''

import turtle
import math
import sys
import striangle


def err_mess():
    '''
    Ends the program when an invalid input is entered
    '''

    print('Make sure you input values in the correct format! \nClose out the program and run it again.')
    sys.exit("Please input values in the correct format! \nClose out the program and run it again.")


#Only runs if main module / It's not imported
if __name__ == "__main__":
    '''
    Initializes the turtle, queries the user for multiple
    inputs for the characteristics of the triangle. Positions the turtle
    so that the triangle will be centered.
    '''

    color_options = ['nofill','fill','rgbfill']
    
    #Program Description. Same one as the description of the project located in the project docstring. Not the function docstring.
    print("This is a recursive program that draws Sierpinski's triangle based off of \na couple of factors: \nHow many degrees does user want to see (iterations) \nDoes user want to see the drawing process \nHow long should one of the sides of the base triangle be \nColor of the triangle\nWhen the program is done drawing the triangle, just click in the window to exit\n")
    
    #Fail safe for incorrect user inputs
    try: 
        deg = int(input("How many degrees (iterations) of Sierpinski's Triangle would you like to see? \nPlease enter an integer. \n"))
        proc = input("Would you like to see the triangle being drawn live? \nPlease enter either 'y' or 'n' \n").lower()
        length = int(input("How long (pixels) would you like to have one of the sides of the base triangle be? \nOtherwise, enter '0' for standard length(500 px) \nPlease enter an integer \n"))
        color = input("Would you like the triangle to have no fill, fill (black), or RGB fill? \nInput is 'nofill', 'fill', 'rgbfill', respectively. \n")
    except:
        print('Make sure you input values in the correct format! \nClose out the program and run it again.')


    #configuring the turtle based off of user input
        

    if length == 0:
        length = 500
    if proc == 'n':
        striangle.pen.speed(0)
        striangle.wn.tracer(0,0)
        striangle.wn.delay(0)
    elif proc != 'y':
        err_mess()
        
    #I'm doing this to check if the user input was valid, also because rgb fill changes color after every triangle so it will be sent into the triangle function 
    if color in color_options:
        #MOVE turtle pen to the left by half of the length and down by length/4 * sqrt3
        #This basically centers the triangle
        
        striangle.pen.up()
        striangle.pen.goto(striangle.pen.xcor()-length/2,striangle.pen.ycor()-length/4*3**(1/2))
        striangle.pen.down()
        striangle.triangle(deg,length,color)
        striangle.wn.exitonclick()
    else:
        err_mess()
    

