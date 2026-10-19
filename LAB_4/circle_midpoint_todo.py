"""Lab 3 - STUDENT FILE: write the midpoint circle algorithm yourself.

Fill in the two TODO sections:
    TODO 1: eight_points()     - the 8 symmetric points of (x, y)
    TODO 2: midpoint_octant()  - the midpoint circle loop for one octant

Everything else (window, grid, checking) is ready.
Run the file: it first CHECKS your answers against the r = 10 example from Lecture 5,
then opens the window.

Formulas (Lecture 5):
    start at (0, r),  p0 = 1 - r
    while x <= y:
        save (x, y)
        if p < 0:   p = p + 2x + 3            -> E,  y stays
        else:       p = p + 2(x - y) + 5      -> SE, y = y - 1
        x = x + 1
    (use x and y BEFORE you change them)
"""
import sys, math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID = 50
CELL = 12
xc, yc, r = 25, 25, 10


def eight_points(xc, yc, x, y):
    """Return a list of the 8 symmetric points of (x, y) around the centre (xc, yc).

    Hint: (x, y) gives (+-x, +-y) and (+-y, +-x). Add xc to every x and yc to every y.
    Example: centre (0, 0), point (3, 9) ->
             (3, 9) (9, 3) (-3, 9) (-9, 3) (3, -9) (9, -3) (-3, -9) (-9, -3)
    """
    points = []
    # ---------------- TODO 1: write your code here ----------------
    # points.append((xc + x, yc + y))
    # ... 7 more ...

    # ---------------------------------------------------------------
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))
    points.append((xc + y, yc + x))
    points.append((xc - y, yc + x))
    points.append((xc + y, yc - x))
    points.append((xc - y, yc - x))
    
    return points


def midpoint_octant(r):
    """Return the list of octant pixels [(x, y), ...] from (0, r) to the 45 degree line."""
    octant = []
    x, y = 0, r
    p = 1 - r
    # ---------------- TODO 2: write your code here ----------------
    # while x <= y:
    #     octant.append((x, y))
    #     ... decide E or SE, update p (and y), then x = x + 1 ...

    # ---------------------------------------------------------------
    while x <= y:
        octant.append((x, y))
        if p < 0:
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y -= 1
        x += 1
    return octant


def midpoint_circle(xc, yc, r):
    pixels = []
    for x, y in midpoint_octant(r):
        pixels.extend(eight_points(xc, yc, x, y))
    return pixels


# ---------------- self check (do not change) ----------------
def check():
    ok = True
    want_octant = [(0, 10), (1, 10), (2, 10), (3, 10), (4, 9), (5, 9), (6, 8), (7, 7)]
    got = midpoint_octant(10)
    if got == want_octant:
        print("TODO 2 correct: octant for r = 10 matches Lecture 5.")
    else:
        ok = False
        print("TODO 2 not yet. Expected", want_octant)
        print("               You gave", got)
    want_8 = {(3, 9), (9, 3), (-3, 9), (-9, 3), (3, -9), (9, -3), (-3, -9), (-9, -3)}
    got8 = eight_points(0, 0, 3, 9)
    if len(got8) == 8 and set(got8) == want_8:
        print("TODO 1 correct: 8 symmetric points of (3, 9).")
    else:
        ok = False
        print("TODO 1 not yet. Expected", sorted(want_8))
        print("               You gave", got8)
    if ok:
        print("Both correct. Press + and - to try other radii.\n")
    return ok


# ---------------- drawing (ready for you) ----------------
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


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()
    plot(midpoint_circle(xc, yc, r), 0.10, 0.60, 0.30)
    true_circle(xc, yc, r)
    glFlush()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    gluOrtho2D(-0.5, GRID - 0.5, -0.5, GRID - 0.5)
    glMatrixMode(GL_MODELVIEW)


def main():
    check()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(GRID * CELL, GRID * CELL)
    glutCreateWindow(b"Lab 3: my midpoint circle")
    glClearColor(1, 1, 1, 1)
    glPointSize(CELL - 1)
    glutDisplayFunc(display); glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
