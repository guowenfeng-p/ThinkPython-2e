import turtle,math


bob = turtle.Turtle()
print(bob)
# 封装
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# square(bob)
# 泛化：为函数增加一个形参被称作
def polygon(t, n, length):
    '''
        绘制一个n边形
    '''
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# polygon(bob, 10, 70)
polygon(bob, n=7, length=70)    #关键字实参 
turtle.mainloop()