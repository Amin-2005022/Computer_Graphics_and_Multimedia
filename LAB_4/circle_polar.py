"""Lab 3 - Circle by the POLAR (trigonometric) method.

    x = r cos(theta),   y = r sin(theta)

We step the angle theta from 0 to 360 degrees.
  - Big step (e.g. 15 degrees): GAPS between pixels.
  - Small step (e.g. 1 degree): no gaps, but many REPEATED pixels (wasted work).
"""
import sys, math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID = 50
CELL = 12
xc, yc, r = 25, 25, 15
step_deg = 10      # angle step in degrees


def round_half_up(v):
    return math.floor(v + 0.5)


def polar_circle(xc, yc, r, step_deg):
    """Return the pixels of the circle using x = r cos t, y = r sin t."""
    pixels = []
    theta = 0.0
    while theta < 360:
        t = math.radians(theta)
        x = round_half_up(r * math.cos(t))
        y = round_half_up(r * math.sin(t))
        pixels.append((xc + x, yc + y))
        theta += step_deg
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
    glColor3f(0.85, 0.5, 0.17)
    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        t = math.radians(i)
        glVertex2f(xc + r * math.cos(t), yc + r * math.sin(t))
    glEnd()


def report():
    pixels = polar_circle(xc, yc, r, step_deg)
    print(f"r = {r}, step = {step_deg} deg: {len(pixels)} points computed, "
          f"{len(set(pixels))} different pixels, {len(pixels) - len(set(pixels))} repeated")


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    plot(polar_circle(xc, yc, r, step_deg), 0.55, 0.20, 0.60)   # purple pixels
    true_circle(xc, yc, r)
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    gluOrtho2D(-0.5, GRID - 0.5, -0.5, GRID - 0.5)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(GRID * CELL, GRID * CELL)
    glutCreateWindow(b"Lab 3: polar method  x = r cos t, y = r sin t")
    glClearColor(1, 1, 1, 1)
    glPointSize(CELL - 1)
    glutDisplayFunc(display); glutReshapeFunc(reshape)
    report()
    glutMainLoop()


if __name__ == "__main__":
    main()
