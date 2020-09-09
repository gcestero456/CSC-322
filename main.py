from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width, height = 500, 500  # window size


def drawSquare(x, y, width, height):
    glBegin(GL_QUADS)  # start drawing a square
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing


def drawTriangle(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glEnd()


def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    #right foot
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(190, 10, 40, 15)

    #left foot
    glColor3f(1.0, 1.0, 0.0)  # set color to GREEN
    drawSquare(110, 10, 40, 15)  # draw a square at (50,50) with width 200, height 200

    #right leg
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(190, 10, 15, 125)

    #left leg
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(135, 10, 15, 125)

    #torso
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(129, 125, 80, 150)

    #neck
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(165, 275, 13, 20)

    #head
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(147, 295, 50, 50)

    #arms
    glColor3f(1.0, 1.0, 0.0)
    drawSquare(38, 225, 250, 15)

    #left eye
    glColor3f(1.0, 0.0, 0.0)
    drawSquare(155, 325, 10, 10)

    #right eye
    glColor3f(1.0, 0.0, 0.0)
    drawSquare(180, 325, 10, 10)

    #mouth
    glColor3f(1.0, 0.0, 0.0)
    drawSquare(157, 300, 30, 7)

    #left fist
    glColor3f(1.0, 0.0, 0.0)
    drawSquare(30, 220, 25, 25)

    #right fist
    glColor3f(1.0, 0.0, 0.0)
    drawSquare(285, 220, 25, 25)



    #glColor3f(1.0, 0.0, 0.0)  # set color to red
    #drawTriangle(300, 250, 200, 200)  # draw a triangle at (300,50)

    glutSwapBuffers()  # important for double buffering


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# initialization
glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("CSC 322 Fall 2020 HW1")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)  # draw all the time
glutMainLoop()  # start everything