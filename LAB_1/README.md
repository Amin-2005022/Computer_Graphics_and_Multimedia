# LAB 1 – First OpenGL programs

Three minimal PyOpenGL + GLUT programs that open a 500x500 window and draw a white shape on a black background using OpenGL's built-in primitives.

## Install

```
pip install PyOpenGL PyOpenGL_accelerate
```

or

```
python -m pip install PyOpenGL PyOpenGL_accelerate
```

> **Windows note:** GLUT needs `freeglut.dll`. If you get a `NullFunctionPointer` / "GLUT not found" error, download freeglut and put `freeglut.dll` in a folder on your `PATH` or next to the script.

## Files

| File            | What it does                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| `line.py`     | Draws a single horizontal white line from (-0.8, 0) to (0.8, 0) using`GL_LINES`.                       |
| `triangle.py` | Draws a filled white triangle with vertices (-0.5, -0.5), (0.5, -0.5), (0.0, 0.5) using`GL_TRIANGLES`. |
| `circle.py`   | Draws a white circle outline (radius 0.5, centred at the origin) as a 100-sided `GL_LINE_LOOP`, with points from `cos`/`sin`. |

All three files share the same structure:

- `init()` – sets the clear colour (black) and the drawing colour (white).
- `display()` – clears the screen and draws the shape.
- `reshape()` – keeps the viewport and a 2D orthographic projection (-1..1 on both axes) correct when the window is resized.
- `main()` – creates the GLUT window and starts the event loop.

## Run

From inside the `LAB_1` folder:

```
python line.py
python triangle.py
python circle.py
```

(or `py <file>.py` on Windows). Close the window to exit.
