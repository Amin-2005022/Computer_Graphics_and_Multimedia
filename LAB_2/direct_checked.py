"""Direct method (checks slope) + OpenGL drawing in one file.
"""
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

X1, Y1, X2, Y2 = 2, 3, 25, 40      # steep line to show the |m| > 1 branch
GRID = 50          # world is 0..GRID in both axes
SHOW_GRID = True        # draw the pixel grid
SHOW_TRUE_LINE = False  # draw the ideal (mathematical) line on top of the pixels


def round_half_up(v):
    return math.floor(v + 0.5)


def direct_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    pixels = []

    if abs(dx) >= abs(dy):
        # gentle line (|m| <= 1): move one step in x, calculate y
        # y = m*x + b
        m = dy / dx if dx != 0 else 0   # dx == 0 only when both points are equal
        b = y1 - m * x1

        step = 1 if x2 >= x1 else -1
        for x in range(x1, x2 + step, step):
            y = m * x + b
            pixels.append((x, round_half_up(y)))
    else:
        # steep line (|m| > 1): move one step in y, calculate x
        # x = (y - b) / m, which is the same as x = x1 + (y - y1) / m
        step = 1 if y2 >= y1 else -1
        for y in range(y1, y2 + step, step):
            if dx == 0:                 # vertical line: x never changes
                x = x1
            else:
                m = dy / dx
                x = x1 + (y - y1) / m
            pixels.append((round_half_up(x), y))

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
    for x, y in direct_line(X1, Y1, X2, Y2):
        glVertex2f(x, y)
    glEnd()
    if SHOW_TRUE_LINE:
        draw_true_line(X1, Y1, X2, Y2)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Direct Line (checked)")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, GRID, -1, GRID)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
