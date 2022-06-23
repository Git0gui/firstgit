import turtle
import cv2 as cv
import numpy as np

#path=input('请输入图片路径')
path = 'D:\python\画布\love.jpg'
src=cv.imread(path)
#print(src.shape)
cv.imshow('s1',src)
width=src.shape[1]
hight=src.shape[0]
print(width,hight)
turtle.setup(width+15,hight+15)
turtle.bgcolor(0,0,0)
turtle.pencolor(1,1,1)
  
    
def y(x,y):
    x=x-1/2*width
    y=-(y-1/2*hight)
    return x,y

gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
ret,image=cv.threshold(gray,0,255,cv.THRESH_OTSU)

"""#找轮廓"""
counters,re=cv.findContours(image,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print('轮廓个数：',len(counters))

for i, con in enumerate(counters):

    area = cv.contourArea(con)

    con = np.reshape(con, (con.shape[0], 2))

    turtle.goto(y(con[0, 0], con[0, 1]))
    turtle.pendown()

    biao_x1 = np.argmin(con[:, 0])
    x1 = con[biao_x1, 0]
    y1 = con[biao_x1, 1]
    # print('x1,y1=',x1,y1)

    biao_x2 = np.argmax(con[:, 0])
    x2 = con[biao_x2, 0]
    y2 = con[biao_x2, 1]
    # print('x2,y2=', x2, y2)

    biao_y3 = np.argmin(con[:, 1])
    x3 = con[biao_y3, 0]
    y3 = con[biao_y3, 1]
    # print('x3,y3=', x3, y3)
    # 下边坐标
    biao_y4 = np.argmin(con[:, 1])
    x4 = con[biao_y4, 0]
    y4 = con[biao_y4, 1]
    # print('x4,y4=', x4, y4)

    x1 = x1
    # right
    x2 = x2
    # up
    y3 = y3
    # bottom
    y4 = y4
    print('x1,y1=', x1, y1)
    print('x2,y2=', x2, y2)
    print('x3,y3=', x3, y3)
    print('x4,y4=', x4, y4)
    if x1 < width and x2 >= 0 and y3 < hight and y4 >= 0:
        a1 = image[y1, x1] / 255

        a2 = image[y2, x2] / 255

        a3 = image[y3, x3] / 255

        a4 = image[y4, x4] / 255
    else:
        a1 = a2 = a3 = a4 = 0

    a = a1 + a2 + a3 + a4

    turtle.begin_fill()

    if a > 5:
        turtle.fillcolor(1, 1, 1)
    elif a <= 5:
        turtle.fillcolor(0, 0, 0)
    # 画图
    for shu, c in enumerate(con):
        turtle.goto(y(c[0], c[1]))
    turtle.goto(y(con[0, 0], con[0, 1]))
    turtle.end_fill()
    turtle.penup()

turtle.mainloop()
