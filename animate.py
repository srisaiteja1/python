import turtle
import random
turtle.bgcolor("black")

turtle.speed(0)
arrow=turtle.Turtle()
turtle.shape("turtle")
width=5
height=7
dot_distance=25
arrow.setpos(-250,250)
arrow.penup()
colourlist=["white","orange","red","blue","indigo","yellow","pink","violet","green"]

def spiral(m,n):
    k=0
    l=0
    flag=0
    col=random.randint(0, 8)
    
    arrow.color(colourlist[col])

    #k is starting index of rows
    #l is starting index of column
    while(k<m and l<n):
        if(flag==1):
            arrow.right(90)
        #printing the elements of first row
        for i in range(l,n):
            arrow.dot()
            arrow.forward(dot_distance)
            # print(a[k][i],end=" ")
        k=k+1
        flag=1
        arrow.right(90)
        col=random.randint(0, 8)
        arrow.color(colourlist[col])
        #printing elements of last column
        for i in range(k,m):
           arrow.dot() 
           arrow.forward(dot_distance) # print(a[i][n-1],end=" ")
        n=n-1
        arrow.right(90)
        col=random.randint(0, 8)
        arrow.color(colourlist[col])
        if(k<m):
            #printing last row in reverse order
            for i in range(n-1,l-1,-1):
               arrow.dot() 
               arrow.forward(dot_distance) # print(a[m-1][i],end=" ")
        m-=1
        arrow.right(90)
        col=random.randint(0, 8)
        arrow.color(colourlist[col])

        if(l<n):
            for i in range(m-1,k-1,-1):
                arrow.dot()
                arrow.forward(dot_distance) # print(a[i][l],end=" ")
            l=l+1

spiral(20,20)
turtle.done()
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()