# LAB 3 – Midpoint line algorithm

Plots a line with the midpoint algorithm as large white points over a pixel grid, using PyOpenGL + GLUT (600x600 window, world coordinates -1..50 on both axes).

## Install

```
pip install PyOpenGL PyOpenGL_accelerate
```

or

```
python -m pip install PyOpenGL PyOpenGL_accelerate
```

> **Windows note:** GLUT needs `freeglut.dll`. If you get a "GLUT not found" / `NullFunctionPointer` error, put `freeglut.dll` in a folder on your `PATH` or next to the script.

## Files

| File | Algorithm | What it does |
|------|-----------|--------------|
| `midpoint.py` | Midpoint line | After each pixel, chooses between E `(x+1, y)` and NE `(x+1, y+1)` by testing which side of the line the midpoint `(x+1, y+0.5)` lies on. Uses integers only: initial `d = 2dy - dx`, `delE = 2dy` (choose E, y stays) and `delNE = 2(dy - dx)` (choose NE, y + 1). Gives the same pixels as basic Bresenham. Only valid for `x1 < x2` and `0 <= m <= 1`. Default line: (2,3) → (40,25). |

The file contains: `midpoint_line()` (returns a list of `(x, y)` pixels), `draw_grid()`, `draw_true_line()`, `display()` and `main()`. The end points are the constants `X1, Y1, X2, Y2` at the top – edit them to try other lines (keep `x1 < x2` and a slope between 0 and 1).

## Display options

| Variable | Default | Meaning |
|----------|---------|---------|
| `SHOW_GRID` | `True` | Draw the pixel grid (grey lines) behind the pixels. |
| `SHOW_TRUE_LINE` | `False` | Draw the ideal mathematical line in orange on top of the pixels. Set to `True` to turn it on. |

## Run

From the project root:

```
cd LAB_3
python midpoint.py
```

(or `py midpoint.py` on Windows). Close the window to exit.
