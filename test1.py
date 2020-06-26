import turtle
import time
'''
1. 画布(canvas)
1.1 设置画布大小
    turtle.screensize(canvwidth=None, canvheight=None, bg=None)
    参数分别为画布的宽(单位像素), 高, 背景颜色
    
    turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
    参数: width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
    (startx, starty): 这一坐标表示 矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心
'''
turtle.screensize(800, 600, "green")
turtle.setup(width=0.6, height=0.6)
'''
2. 画笔
    2.1 画笔的状态
    1. turtle.pensize()：设置画笔的宽度；
    2. turtle.pencolor(); 没有参数传入,返回当前画笔颜色,传入参数设置画笔颜色,可以是字符串如"green", "red",也可以是RGB 3元组,
        >>> pencolor('brown')
        >>> tup = (0.2, 0.8, 0.55)
        >>> pencolor(tup)
        >>> pencolor()
        '#33cc8c'
    3.turtle.speed(speed): 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
'''

time.sleep(10)