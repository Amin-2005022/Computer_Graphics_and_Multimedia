"""Bresenham for every slope and direction + OpenGL drawing in one file.
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

X1, Y1, X2, Y2 = 40, 5, 10, 45     # any slope / direction works
GRID = 50          # world is 0..GRID in both axes
SHOW_GRID = True        # draw the pixel grid
SHOW_TRUE_LINE = False  # draw the ideal (mathematical) line on top of the pixels


def bresenham_any(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1
    pixels = [(x, y)]
    if dx >= dy:                        # gentle: step x, decide y
        d = 2 * dy - dx
        for _ in range(dx):
            if d < 0:
                d += 2 * dy
            else:
                d += 2 * (dy - dx)
                y += sy
            x += sx
            pixels.append((x, y))
    else:                               # steep: step y, decide x
        d = 2 * dx - dy
        for _ in range(dy):
            if d < 0:
                d += 2 * dx
            else:
                d += 2 * (dx - dy)
                x += sx
            y += sy
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
    for x, y in bresenham_any(X1, Y1, X2, Y2):
        glVertex2f(x, y)
    glEnd()
    if SHOW_TRUE_LINE:
        draw_true_line(X1, Y1, X2, Y2)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Bresenham Line (any slope)")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, GRID, -1, GRID)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
