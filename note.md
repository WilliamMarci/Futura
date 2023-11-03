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
# Code

## Python

### function
匿名函数
```python
lambda [arg1 [,arg2,.....argn]]:expression
```

## Animetion

```python
self.add(Object)            #添加对象
self.play(Write(text))      #写文字
self.play(Create(Object))   #创建对象的动画
self.play(FadeOut(Object))  #淡出
self.play(Transform(Object1,Object2))#变换
def update_fun(mob):
    mob.method(var)
mobject.add_updater(update_fun)
```

有多个对象的时候可以把`update_fun`封装起来
```python
def update_fun(para1): #传入参数
    def anim(obj,dt):
        obj.method(para1,dt)
    return anim
```

可以打包然后动画

```python
group=Group()
group.add(object)
self.play(*[AnimeClass(mob) for mob in group])
```

## Text and Formular
### text
文字
```python
text = Text("X position", font="Times New Roman").scale(0.75)
```
数字
```python
label = DecimalNumber()
```
### formular
公式

```python
fomular=MathTex(r"\sin\theta_C=\frac{1}{n}").shift(1*DOWN+5*RIGHT)
```


## Object Operation

## Math Function

all from [Document](https://docs.manim.community/en/stable/index.html)

### dot product of matrix
矩阵相乘
use `@`

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = a @ b
```

### rotate vector
矢量绕轴旋转
```python
rotate_vector(vector,angle,axis)
```

### line intersection
两直线交点
```python
line_intersection(line1,line2)
```

### middle point
线段中点
```python
midpoint(point1, point2)
```

### Numper plane
坐标网
```python
plane=NumberPlane()
plane.add_coordinates(x,y)#坐标
```