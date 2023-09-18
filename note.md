# The Structure

this is the note for recode the tutor of manim.

## Head 

If you want build a manim project, for our scr, we must import it as :

```python
from manim import *
class ClassName(Sence): 
    def construct(self):
        ...
```
we use `construct()` method of class `Scene`

## Build

To build the manim project, we just launch the terminal and type:

```shell
manim -ql filename.py ClassName
```


