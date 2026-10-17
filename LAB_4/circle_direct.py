"""Lab 3 - Circle by the DIRECT (polynomial) method.

    y = round( sqrt(r*r - x*x) )

We step x by 1 from -r to r and compute y for the top and bottom halves.
Look near the left and right ends: the circle is steep there, so pixels have GAPS.
"""
import sys, math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID = 50          # logical pixels across and down
CELL = 12          # screen pixels per logical pixel
xc, yc, r = 25, 25, 15


def round_half_up(v):
    """Round the way we do in class: 0.5 always rounds up."""
    return math.floor(v + 0.5)


def direct_circle(xc, yc, r):
    """Return the pixels of the circle using y = sqrt(r^2 - x^2)."""
    pixels = []
    for x in range(-r, r + 1):              # step x by 1
        y = round_half_up(math.sqrt(r * r - x * x))
        pixels.append((xc + x, yc + y))     # top half
        pixels.append((xc + x, yc - y))     # bottom half
    return pixels


# ---------------- drawing ----------------
def draw_grid():
    glColor3f(0.85, 0.85, 0.85)
    glBegin(GL_LINES)
    for i in range(GRID + 1):
        glVertex2f(i - 0.5, -0.5); glVertex2f(i - 0.5, GRID - 0.5)
        glVertex2f(-0.5, i - 0.5); glVertex2f(GRID - 0.5, i - 0.5)
    glEnd()


def plot(pixels, red, green, blue):
    glColor3f(red, green, blue)
    glBegin(GL_POINTS)
    for x, y in pixels:
        glVertex2i(x, y)
    glEnd()


def true_circle(xc, yc, r):
    glColor3f(0.85, 0.5, 0.17)              # orange: the mathematical circle
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        t = math.radians(i)
        glVertex2f(xc + r * math.cos(t), yc + r * math.sin(t))
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    plot(direct_circle(xc, yc, r), 0.12, 0.31, 0.60)   # blue pixels
    true_circle(xc, yc, r)
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    gluOrtho2D(-0.5, GRID - 0.5, -0.5, GRID - 0.5)   # 1 unit = 1 logical pixel
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(GRID * CELL, GRID * CELL)
    glutCreateWindow(b"Lab 3: direct method  y = sqrt(r^2 - x^2)")
    glClearColor(1, 1, 1, 1)
    glPointSize(CELL - 1)
    glutDisplayFunc(display); glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
