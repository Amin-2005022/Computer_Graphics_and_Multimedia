"""Basic Bresenham line (0 <= m <= 1, x1 < x2) + OpenGL drawing in one file.
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# line endpoints (must satisfy x1 < x2 and 0 <= slope <= 1)
X1, Y1, X2, Y2 = 2, 3, 40, 25
GRID = 50          # world is 0..GRID in both axes
SHOW_GRID = True        # draw the pixel grid
SHOW_TRUE_LINE = False  # draw the ideal (mathematical) line on top of the pixels


def bresenham_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx                     # initial decision parameter
    inc1 = 2 * dy                       # added when we choose S (y stays)
    inc2 = 2 * (dy - dx)                # added when we choose T (y + 1)
    x, y = x1, y1
    pixels = [(x, y)]
    while x < x2:
        if d < 0:
            d += inc1
        else:
            d += inc2
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
    for x, y in bresenham_line(X1, Y1, X2, Y2):
        glVertex2f(x, y)
    glEnd()
    if SHOW_TRUE_LINE:
        draw_true_line(X1, Y1, X2, Y2)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Bresenham Line")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1, GRID, -1, GRID)
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
