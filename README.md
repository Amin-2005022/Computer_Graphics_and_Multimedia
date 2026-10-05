# Computer_Graphics_and_Multimedia

Python + OpenGL (PyOpenGL / GLUT) lab programs for the Computer Graphics and Multimedia course.

| Folder    | Contents                                                                        |
| --------- | ------------------------------------------------------------------------------- |
| `LAB_1` | First OpenGL programs: line, triangle, circle                                   |
| `LAB_2` | Line drawing algorithms: DDA, direct method, Bresenham, and a comparison viewer |

See the `README.md` inside each folder for a description of every file.

## Install

Run one of these (they do the same thing):

```
pip install PyOpenGL PyOpenGL_accelerate
```

```
python -m pip install PyOpenGL PyOpenGL_accelerate
```

> **Windows note:** GLUT needs `freeglut.dll`. If you get a "GLUT not found" / `NullFunctionPointer` error, put `freeglut.dll` in a folder on your `PATH` or next to the scripts.

## Run

Open a terminal in the project root (the folder containing `LAB_1` and `LAB_2`), enter a lab folder with `cd`, then run a file with `python`. Close the window to exit.

### LAB_1

```
cd LAB_1
python line.py
python triangle.py
python circle.py
```

### LAB_2

```
cd LAB_2
python dda.py
python direct_simple.py
python direct_checked.py
python bresenham.py
python bresenham_any.py
python compare.py
```

`compare.py` imports the other files in `LAB_2`, so it must be run from inside that folder.

Each LAB_2 file has two display switches at the top: `SHOW_GRID` (default `True`) draws the pixel grid, and `SHOW_TRUE_LINE` (default `False`) draws the ideal mathematical line in orange. Set it to `True` to see it.

To go back to the project root, or move from one lab to the other:

```
cd ..
```

On Windows you can use `py` instead of `python` (e.g. `py line.py`).
