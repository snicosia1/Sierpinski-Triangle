from turtle import *
S_T = Turtle()
def draw_triangle(x1,y1,x2,y2,x3,y3):
    S_T.penup()
    S_T.goto(x1,y1)
    S_T.pendown()
    S_T.goto(x2,y2)
    S_T.goto(x3,y3)
    S_T.goto(x1,y1)
    S_T.speed(0)
def mid(p1,p2):
    L = ((p1+p2)/2)
    return L

p_points = [[-350,-300,350,-300,0,300]]

c_points = [[-350,-300,350,-300,0,300]]
y = 0
n = 4
for i in range(n):
    t = 0
    for x in range(len(c_points)):
        t1x1 = c_points[t][0]
        t1y1 = c_points[t][1]
        t1x2 = mid(c_points[t][0],c_points[t][2])
        t1y2 = c_points[t][3]
        t1x3 = mid(c_points[t][0],c_points[t][4])
        t1y3 = mid(c_points[t][1],c_points[t][-1])

        t2x1 = t1x2
        t2y1 = t1y2
        t2x2 = c_points[t][2]
        t2y2 = c_points[t][3]
        t2x3 = mid(c_points[t][2],c_points[t][4])
        t2y3 = mid(c_points[t][3],c_points[t][5])

        t3x1 = t2x3
        t3y1 = t2y3
        t3x2 = t1x3
        t3y2 = t1y3
        t3x3 = c_points[t][4]
        t3y3 = c_points[t][5]
        c_points.append([t1x1, t1y1, t1x2, t1y2, t1x3, t1y3])
        c_points.append([t2x1, t2y1, t2x2, t2y2, t2x3, t2y3])
        c_points.append([t3x1, t3y1, t3x2, t3y2, t3x3, t3y3])
        p_points.append([t1x1, t1y1, t1x2, t1y2, t1x3, t1y3])
        p_points.append([t2x1, t2y1, t2x2, t2y2, t2x3, t2y3])
        p_points.append([t3x1, t3y1, t3x2, t3y2, t3x3, t3y3])
        print(p_points)
        t += 1

for x in p_points:
    x1 = p_points[y][0]
    y1 = p_points[y][1]
    x2 = p_points[y][2]
    y2 = p_points[y][3]
    x3 = p_points[y][4]
    y3 = p_points[y][5]
    y += 1
    draw_triangle(x1, y1, x2, y2, x3, y3)








done()














