"""Lab 4 - MINI PAINT (STUDENT FILE): a drawing tool built only from our own algorithms.

YOUR JOB: fill in the 3 TODO sections in the ELLIPSE part below.
When you run the file it first CHECKS your ellipse against the a = 8, b = 6 example
from Lecture 6. Line, circle, pencil and fill already work: try them first.

Every shape is drawn pixel by pixel with the algorithms from class:
    line    -> Bresenham (all slopes)
    circle  -> midpoint circle + 8-way symmetry
    ellipse -> midpoint ellipse (two regions) + 4-way symmetry
    pencil  -> Bresenham lines between mouse positions
    fill    -> flood fill (bonus, preview of the next lecture)

MOUSE
    Line:    click start, click end
    Circle:  click centre, click a point on the circle
    Ellipse: click centre, click a corner (a = |dx|, b = |dy|)
    Pencil:  hold the left button and drag
    Fill:    click inside a closed shape
    The shape follows the mouse before the second click (rubber band).

KEYBOARD
    L line   C circle   E ellipse   P pencil   F fill
    1-6 colour   Z undo   X clear   G grid on/off
    R show ellipse regions (region 1 blue, region 2 green)
    Esc cancel the shape you started   Q quit
"""
import sys, math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID_W, GRID_H = 80, 60          # logical pixels
CELL = 10                        # screen pixels per logical pixel
COLOURS = {b"1": (0.0, 0.0, 0.0), b"2": (0.85, 0.15, 0.15), b"3": (0.10, 0.55, 0.25),
           b"4": (0.12, 0.31, 0.75), b"5": (0.95, 0.60, 0.05), b"6": (0.55, 0.20, 0.60)}
NAMES = {b"1": "black", b"2": "red", b"3": "green", b"4": "blue", b"5": "orange", b"6": "purple"}

tool = "line"                    # line, circle, ellipse, pencil, fill
colour_key = b"1"
shapes = []                      # list of (pixels, colour); the picture is redrawn from this list
start = None                     # first click of a two-click shape
mouse = None                     # current mouse position (for the rubber band)
show_grid = True
show_regions = False
win_w, win_h = GRID_W * CELL, GRID_H * CELL


# =============== ALGORITHMS (from the lectures) ===============
def bresenham_line(x1, y1, x2, y2):
    """Bresenham for every slope and direction."""
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1
    pixels = [(x, y)]
    if dx >= dy:                              # gentle: step x
        d = 2 * dy - dx
        for _ in range(dx):
            if d < 0: d += 2 * dy
            else: d += 2 * (dy - dx); y += sy
            x += sx
            pixels.append((x, y))
    else:                                     # steep: step y
        d = 2 * dx - dy
        for _ in range(dy):
            if d < 0: d += 2 * dx
            else: d += 2 * (dx - dy); x += sx
            y += sy
            pixels.append((x, y))
    return pixels


def eight_points(xc, yc, x, y):
    return [(xc + x, yc + y), (xc + y, yc + x), (xc - x, yc + y), (xc - y, yc + x),
            (xc + x, yc - y), (xc + y, yc - x), (xc - x, yc - y), (xc - y, yc - x)]


def midpoint_circle(xc, yc, r):
    x, y, p = 0, r, 1 - r
    pixels = []
    while x <= y:
        pixels += eight_points(xc, yc, x, y)
        if p < 0: p += 2 * x + 3
        else: p += 2 * (x - y) + 5; y -= 1
        x += 1
    return pixels


def four_points(xc, yc, x, y):
    """Return the 4 symmetric points of (x, y) around the centre (xc, yc): (xc +- x, yc +- y)."""
    points = []
    # ---------------- TODO 1: the 4 symmetric points ----------------

    # -----------------------------------------------------------------
    return points


def midpoint_ellipse_quadrant(a, b):
    """Return (region1, region2): quadrant pixels from (0, b) to (a, 0).

    Lecture 6 formulas (x, y are the NEW values after each step):
      Region 1, while 2b^2 x < 2a^2 y:
          x = x + 1
          if p1 < 0:  p1 = p1 + 2b^2 x + b^2                  (E)
          else:       y = y - 1;  p1 = p1 + 2b^2 x - 2a^2 y + b^2   (SE)
      Region 2, while y > 0:
          y = y - 1
          if p2 > 0:  p2 = p2 - 2a^2 y + a^2                   (S)
          else:       x = x + 1;  p2 = p2 + 2b^2 x - 2a^2 y + a^2   (SE)
    """
    a2, b2 = a * a, b * b
    x, y = 0, b
    px, py = 0, 2 * a2 * y                    # running values of 2b^2 x and 2a^2 y
    region1, region2 = [(x, y)], []
    p1 = b2 - a2 * b + 0.25 * a2              # p1_0 = b^2 - a^2 b + a^2/4
    # ---------------- TODO 2: region 1 loop ----------------
    # while px < py:
    #     x += 1; px += 2 * b2
    #     ... E or SE (when y goes down: py -= 2 * a2) ...
    #     region1.append((x, y))

    # --------------------------------------------------------
    p2 = b2 * (x + 0.5) ** 2 + a2 * (y - 1) ** 2 - a2 * b2   # p2_0
    # ---------------- TODO 3: region 2 loop ----------------
    # while y > 0:
    #     y -= 1; py -= 2 * a2
    #     ... S or SE (when x goes up: px += 2 * b2) ...
    #     region2.append((x, y))

    # --------------------------------------------------------
    return region1, region2


def check_ellipse():
    """Self check against the Lecture 6 example. Do not change."""
    want1 = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 5), (5, 5), (6, 4), (7, 3)]
    want2 = [(8, 2), (8, 1), (8, 0)]
    r1, r2 = midpoint_ellipse_quadrant(8, 6)
    print("TODO 2 region 1:", "correct" if r1 == want1 else f"not yet. Expected {want1}, you gave {r1}")
    print("TODO 3 region 2:", "correct" if r2 == want2 else f"not yet. Expected {want2}, you gave {r2}")
    got4 = four_points(0, 0, 3, 5)
    ok4 = len(got4) == 4 and set(got4) == {(3, 5), (-3, 5), (3, -5), (-3, -5)}
    print("TODO 1 four points:", "correct" if ok4 else f"not yet. You gave {got4}")
    print()


def midpoint_ellipse(xc, yc, a, b):
    if a == 0 or b == 0:                      # flat ellipse = a line
        return bresenham_line(xc - a, yc - b, xc + a, yc + b)
    r1, r2 = midpoint_ellipse_quadrant(a, b)
    return [p for x, y in r1 + r2 for p in four_points(xc, yc, x, y)]


def flood_fill(seed, canvas):
    """4-connected flood fill with our own stack (no recursion limit).
    canvas: dict pixel -> colour. Returns the pixels to paint."""
    old = canvas.get(seed)
    filled, stack = set(), [seed]
    while stack:
        x, y = stack.pop()
        if (x, y) in filled or not (0 <= x < GRID_W and 0 <= y < GRID_H):
            continue
        if canvas.get((x, y)) != old:
            continue
        filled.add((x, y))
        stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return list(filled)


# =============== TOOLS ===============
def shape_pixels(p0, p1):
    """Pixels of the current tool between the first click p0 and point p1."""
    (x0, y0), (x1, y1) = p0, p1
    if tool == "line":
        return bresenham_line(x0, y0, x1, y1)
    if tool == "circle":
        r = round(math.hypot(x1 - x0, y1 - y0))
        return midpoint_circle(x0, y0, r)
    if tool == "ellipse":
        return midpoint_ellipse(x0, y0, abs(x1 - x0), abs(y1 - y0))
    return []


def canvas_now():
    canvas = {}
    for pixels, colour in shapes:
        for p in pixels:
            canvas[p] = colour
    return canvas


def to_grid(x, y):
    """Window pixel (x down from top) -> grid cell (y up from bottom)."""
    gx = int(x * GRID_W / win_w)
    gy = int((win_h - 1 - y) * GRID_H / win_h)
    return max(0, min(GRID_W - 1, gx)), max(0, min(GRID_H - 1, gy))


# =============== DRAWING ===============
def draw_grid():
    glColor3f(0.88, 0.88, 0.88)
    glBegin(GL_LINES)
    for i in range(GRID_W + 1):
        glVertex2f(i - 0.5, -0.5); glVertex2f(i - 0.5, GRID_H - 0.5)
    for j in range(GRID_H + 1):
        glVertex2f(-0.5, j - 0.5); glVertex2f(GRID_W - 0.5, j - 0.5)
    glEnd()


def plot(pixels, colour):
    glColor3f(*colour)
    glBegin(GL_POINTS)
    for x, y in pixels:
        if 0 <= x < GRID_W and 0 <= y < GRID_H:
            glVertex2i(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if show_grid:
        draw_grid()
    for pixels, colour in shapes:
        plot(pixels, colour)
    if start and mouse and tool in ("line", "circle", "ellipse"):     # rubber band
        if tool == "ellipse" and show_regions:
            a, b = abs(mouse[0] - start[0]), abs(mouse[1] - start[1])
            if a and b:
                r1, r2 = midpoint_ellipse_quadrant(a, b)
                plot([p for x, y in r1 for p in four_points(*start, x, y)], (0.12, 0.31, 0.75))
                plot([p for x, y in r2 for p in four_points(*start, x, y)], (0.10, 0.60, 0.30))
        else:
            c = COLOURS[colour_key]
            plot(shape_pixels(start, mouse), tuple(0.55 + 0.45 * v for v in c))
        plot([start], (0.85, 0.5, 0.17))
    glutSwapBuffers()


def update_title():
    msg = f"Mini Paint | tool: {tool} | colour: {NAMES[colour_key]} | shapes: {len(shapes)}"
    if show_regions: msg += " | regions ON"
    glutSetWindowTitle(msg.encode())


# =============== MOUSE ===============
def mouse_click(button, state, x, y):
    global start, mouse
    if button != GLUT_LEFT_BUTTON:
        return
    g = to_grid(x, y)
    if tool == "pencil":
        if state == GLUT_DOWN:
            start = g; shapes.append(([g], COLOURS[colour_key]))
        else:
            start = None
    elif state == GLUT_DOWN:
        if tool == "fill":
            shapes.append((flood_fill(g, canvas_now()), COLOURS[colour_key]))
        elif start is None:
            start = g                                    # first click
        else:
            shapes.append((shape_pixels(start, g), COLOURS[colour_key]))
            print(f"{tool} from {start} to {g}")
            start = None                                 # second click: shape done
    mouse = g
    update_title(); glutPostRedisplay()


def mouse_drag(x, y):                                    # button held down
    global start, mouse
    g = to_grid(x, y)
    if tool == "pencil" and start is not None and g != start:
        pixels, colour = shapes[-1]
        shapes[-1] = (pixels + bresenham_line(*start, *g)[1:], colour)
        start = g
    mouse = g
    glutPostRedisplay()


def mouse_move(x, y):                                    # no button held
    global mouse
    mouse = to_grid(x, y)
    if start is not None:
        glutPostRedisplay()


# =============== KEYBOARD ===============
def keyboard(key, x, y):
    global tool, colour_key, start, show_grid, show_regions
    k = key.lower()
    tools = {b"l": "line", b"c": "circle", b"e": "ellipse", b"p": "pencil", b"f": "fill"}
    if k in tools: tool = tools[k]; start = None
    elif key in COLOURS: colour_key = key
    elif k == b"z" and shapes: shapes.pop()
    elif k == b"x": shapes.clear()
    elif k == b"g": show_grid = not show_grid
    elif k == b"r": show_regions = not show_regions
    elif key == b"\x1b": start = None
    elif k == b"q": sys.exit(0)
    update_title(); glutPostRedisplay()


def reshape(w, h):
    global win_w, win_h
    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    gluOrtho2D(-0.5, GRID_W - 0.5, -0.5, GRID_H - 0.5)
    glMatrixMode(GL_MODELVIEW)
    glPointSize(max(1, min(w / GRID_W, h / GRID_H) - 1))


def main():
    print(__doc__)
    check_ellipse()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(win_w, win_h)
    glutCreateWindow(b"Mini Paint")
    glClearColor(1, 1, 1, 1)
    glutDisplayFunc(display); glutReshapeFunc(reshape)
    glutMouseFunc(mouse_click); glutMotionFunc(mouse_drag); glutPassiveMotionFunc(mouse_move)
    glutKeyboardFunc(keyboard)
    update_title()
    glutMainLoop()


if __name__ == "__main__":
    main()
