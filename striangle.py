'''
Sierpinski's Triangle by dumblole

This is the function that actually draws Sierpinski's Triangle.
Imported to main.py
This can run by itself but it is recommended to run main.py for a better user experience
NOTE: Does not center the triangle if program was run from here
'''



import turtle
import random


#Declaring variables
wn = turtle.Screen()
pen = turtle.Turtle()
#default color mode is 1
wn.colormode(255)


def triangle(degree,length,color):
    '''
    This is the function that actually draws Sierpinski's Triangle
    
    degree is the amt of iterations
    degree set is just the integer of iterations the user wants to see.
    
    length is the base length of the triangle when first called
    length set is the integer length in pixels for the length of one of the sides of the base equillateral equation
    
    color is whatever the user chooses to fill the triangle
    color can be 'nofill', 'fill', or 'rgbfill'
    '''
        #Color config
    if color == 'nofill':
        pen.fillcolor(255,255,255)
    if color == 'fill':
        pen.fillcolor(0,0,0)
    if color == 'rgbfill':
        pen.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #Base case. If iterations reach zero, then just stop the program
    if degree <= 0 :
        pen.begin_fill()
        for _ in range(3):
            pen.forward(length)
            #We have to turn 120 to make the 60 degree angle for the equillateral triangle
            pen.left(120)
        pen.end_fill()
    else:
        '''
        Calls itself three times, one for each of the three triangles as seen in degree 1
        And for every next degree there will be three more triangles in each of the three triangles and three more for the three triangles in each of the three original triangles and so on.
        Basically, if the function it was calling not on itself but on a different function
        that only drew a triangle, it would be able to draw one degree and reset to the
        bottom left of the triangle which is where the pen started
        Making it recursive makes it able to draw multiple degrees
        It doesn't bother with drawing each degree at a time but instead draws the degree as requested but instead positions the pen every time it calls on itself
        by iterating the degree value to 0 while dividing the length by 2 everytime and moving the pen
        '''
        triangle(degree-1,length/2,color)
        pen.left(60)
        pen.forward(length/2)
        pen.right(60)
        triangle(degree-1,length/2,color)
        pen.left(60)
        pen.backward(length/2)
        pen.right(60)
        pen.forward(length/2)
        triangle(degree-1,length/2,color)
        pen.backward(length/2)
        #Referring back to the comment made eariler, this resets the pen to the bottom left of the triangle

