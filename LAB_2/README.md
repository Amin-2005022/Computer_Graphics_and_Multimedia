# LAB 2 – Line drawing algorithms

Each file implements one line-drawing algorithm and plots the resulting pixels as large white points with PyOpenGL + GLUT (600x600 window, world coordinates -1..50 on both axes). The end points are set by the constants `X1, Y1, X2, Y2` at the top of each file – edit them to try other lines.

## Install

```
pip install PyOpenGL PyOpenGL_accelerate
```

or

```
python -m pip install PyOpenGL PyOpenGL_accelerate
```

> **Windows note:** GLUT needs `freeglut.dll`. If you get a "GLUT not found" / `NullFunctionPointer` error, put `freeglut.dll` in a folder on your `PATH` or next to the scripts.

## Files

| File | Algorithm | What it does |
|------|-----------|--------------|
| `dda.py` | DDA (Digital Differential Analyzer) | Takes `steps = max(abs(dx), abs(dy))`, increments x and y by `dx/steps` and `dy/steps` each step, and rounds to the nearest pixel. Works for any slope/direction. Default line: (2,3) → (40,25). |
| `direct_simple.py` | Direct method (simple) | Uses `y = m·x + b` stepping over x. Handles only the vertical special case (`x1 == x2`). Gaps appear for steep lines (`|m| > 1`). Default line: (2,3) → (40,25). |
| `direct_checked.py` | Direct method (with slope check) | Same equation, but if `|m| <= 1` it steps x and computes y; otherwise it steps y and computes `x = x1 + (y - y1)/m`. Gives a gap-free line for any slope. Default line: (2,3) → (25,40) (steep). |
| `bresenham.py` | Bresenham (basic) | Integer-only decision parameter `d = 2dy - dx`. Only valid for `x1 < x2` and `0 <= m <= 1`. Default line: (2,3) → (40,25). |
| `bresenham_any.py` | Bresenham (all cases) | Generalised Bresenham: uses `abs(dx)`, `abs(dy)` and sign steps, and swaps the roles of x and y for steep lines, so every slope and direction works. Default line: (40,5) → (10,45). |
| `compare.py` | Comparison viewer | Imports the algorithms from the other files and draws four lines on a 50x50 grid of big pixels, with the true mathematical line in orange (only when `SHOW_TRUE_LINE = True`). Keys: `1` DDA (blue), `2` Bresenham (green), `3` both, `4` direct method without slope check (gaps on steep lines), `5` direct method with slope check, `q` quit. Must be run from this folder because it imports its sibling files. |

Each algorithm file contains: the algorithm function (returns a list of `(x, y)` pixels), `draw_grid()`, `draw_true_line()`, `display()` (draws the grid, the pixels as `GL_POINTS`, and optionally the true line), and `main()` (creates the window).

## Display options

Every file in this folder (including `compare.py`) has two switches near the top:

| Variable | Default | Meaning |
|----------|---------|---------|
| `SHOW_GRID` | `True` | Draw the pixel grid (grey lines) behind the pixels. |
| `SHOW_TRUE_LINE` | `False` | Draw the ideal mathematical line in orange on top of the pixels, to see how far the chosen pixels are from it. Set to `True` to turn it on. |

## Run

From inside the `LAB_2` folder:

```
python dda.py
python direct_simple.py
python direct_checked.py
python bresenham.py
python bresenham_any.py
python compare.py
```

(or `py <file>.py` on Windows). Close the window to exit.

Tip: run two of them with the same end points (e.g. `direct_simple.py` vs `direct_checked.py` on a steep line) to compare the output.
