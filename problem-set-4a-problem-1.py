# Problem Set 4A - Problem 1
# CTEC 121
# YOUR NAME

import graphics


def snowman():
    # create the graphics window
    win = graphics.GraphWin('Problem 1 - Snowman', 800, 800)

    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circle3

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    # draw two arms that connect to the body of the snowman
    # name the line objects leftArm and rightArm

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()
