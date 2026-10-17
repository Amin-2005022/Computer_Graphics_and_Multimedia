"""Midpoint line (0 <= m <= 1, x1 < x2) + OpenGL drawing in one file.
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# end points of the line (needs x1 < x2 and slope between 0 and 1)
X1, Y1, X2, Y2 = 2, 3, 40, 25
GRID = 50          # grid size: pixels 0..GRID in x and y
SHOW_GRID = True        # draw the pixel grid
SHOW_TRUE_LINE = False  # draw the ideal (mathematical) line on top of the pixels


def midpoint_line(x1, y1, x2, y2):
    # Midpoint algorithm: after plotting (x, y), the next pixel is either
    #   E  = (x + 1, y)      -> east
    #   NE = (x + 1, y + 1)  -> north-east
    # We test on which side of the line the midpoint M = (x + 1, y + 0.5) lies.
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx                     # decision value d = 2*F(M) for the first step
    delE = 2 * dy                       # change in d if we move E
    delNE = 2 * (dy - dx)               # change in d if we move NE
    x, y = x1, y1
    pixels = [(x, y)]                   # start with the first end point
    while x < x2:
        if d < 0:                       # M is above the line -> line is closer to E
            d += delE
        else:                           # M is on/below the line -> line is closer to NE
            d += delNE
            y += 1
        x += 1
        pixels.append((x, y))
    return pixels


def draw_grid():
    glColor3f(0.25, 0.25, 0.25)
    glLineWidth(1)
    glBegin(GL_LINES)
    for i in range(GRID + 1):
        glVertex2f(i - 0.5, -0.5)
        glVertex2f(i - 0.5, GRID - 0.5)
        glVertex2f(-0.5, i - 0.5)
        glVertex2f(GRID - 0.5, i - 0.5)
    glEnd()


def draw_true_line(x1, y1, x2, y2):
    glColor3f(0.85, 0.3, 0.1)           # orange: the mathematical line
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if SHOW_GRID:
        draw_grid()
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(8)
    glBegin(GL_POINTS)
    for x, y in midpoint_line(X1, Y1, X2, Y2):
        glVertex2f(x, y)
    glEnd()
    if SHOW_TRUE_LINE:
        draw_true_line(X1, Y1, X2, Y2)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Midpoint Line")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, GRID, -1, GRID)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
