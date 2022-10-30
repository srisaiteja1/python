import turtle as turt
import random

colour=["red","blue","green","orange","yellow","violet","cyan"]
wn=turt.Screen()

wn.screensize(300,300)
tur=turt.Turtle()
tur.pensize(2)
tur.penup()
tur.setpos(-200,200)

#draw H
tur.speed(2)
tur.color(colour[random.randint(0, 6)])
tur.penup()
tur.pendown()
tur.right(90)
tur.forward(37)
tur.backward(75)
tur.forward(37)
tur.right(90)
tur.forward(75)
tur.left(90)
tur.forward(37)
tur.backward(75)
tur.penup()

    
tur.setpos(-195,200)
#draw A
tur.color(colour[random.randint(0, 6)])
tur.left(90)
tur.pendown()
tur.forward(65)
tur.right(45)
tur.forward(25)
tur.backward(75)
tur.right(90)
tur.forward(75)

tur.penup()
tur.setpos(-120,195)

#draw P
tur.color(colour[random.randint(0, 6)])
tur.left(135)
tur.pendown()
tur.circle(30,180)
tur.left(90)
tur.forward(90)

#draw another P
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-90,195)
tur.left(90)
tur.pendown()
tur.circle(30,180)
tur.left(90)
tur.forward(90)

tur.penup()
tur.setpos(-60,225)

#draw Y
tur.color(colour[random.randint(0, 6)])
tur.pendown()
tur.left(45)
tur.forward(50)
tur.left(85)
tur.forward(50)
tur.backward(100)


# draw B
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-250,50)
tur.right(45)
tur.pendown()
tur.circle(30,180)
tur.left(95)
tur.forward(60*2)
tur.left(90)
tur.circle(30,180)


#draw I
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-184.77,109.77)
tur.pendown()
tur.left(180)
tur.forward(30)
tur.backward(60)
tur.forward(30)
tur.right(90)
tur.forward(120)
tur.left(90)
tur.forward(30)
tur.backward(60)

#draw R
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-154.77,50.23)
tur.pendown()
tur.circle(30,180)
tur.left(90)
tur.forward(120)
tur.backward(60)
tur.left(45)
tur.forward(70)


#draw T
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-85.27,-3)
tur.pendown()
tur.left(45+90)
tur.forward(115)
tur.left(90)
tur.forward(30)
tur.backward(60)
tur.penup()
#draw H
tur.setpos(-55.27,52)
tur.color(colour[random.randint(0, 6)])
tur.pendown()
tur.right(90)
tur.forward(60)
tur.backward(120)
tur.forward(60)
tur.right(90)
tur.forward(60)
tur.left(90)
tur.forward(60)
tur.backward(120)
#draw D
tur.color(colour[random.randint(0, 6)])
tur.right(90)
tur.circle(60,180)

tur.penup()
#draw A
tur.color(colour[random.randint(0, 6)])
tur.setposition(104.73,112-60)
tur.left(180)
tur.pendown()
tur.forward(80)
tur.right(65)
tur.forward(50)
tur.backward(150)
tur.right(50)
tur.forward(150)

tur.penup()
#draw Y
tur.color(colour[random.randint(0, 6)])
tur.setpos(214.73,120)
tur.left(65)
tur.pendown()
tur.forward(70)
tur.left(95)
tur.forward(70)
tur.backward(120)

# draw N
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-250,-190)
tur.pendown()
tur.left(45)
tur.forward(100)
tur.right(45+90)
tur.forward(141.42)
tur.left(45+90)
tur.forward(100)

#draw A
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-120,-140)

tur.right(90)
tur.pendown()
tur.forward(80)
tur.right(65)
tur.forward(50)
tur.backward(150)
tur.right(50)
tur.forward(150)

#draw V
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(-17.28,-75.36)
tur.pendown()
tur.left(55)
tur.forward(120)
tur.left(120)
tur.forward(120)

#Draw Y
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(104.72,-80.36)
tur.right(100)
tur.pendown()
tur.forward(70)
tur.left(95)
tur.forward(70)
tur.backward(120)

#Draw A
tur.penup()
tur.color(colour[random.randint(0, 6)])
tur.setpos(194.36,-129.34)
tur.right(55)
tur.pendown()
tur.forward(80)
tur.right(65)
tur.forward(50)
tur.backward(150)
tur.right(50)
tur.forward(150)
tur.penup()
tur.setpos(310,150)
tur.right(250)
tur.pendown()
tur.color('red', 'yellow')
tur.begin_fill()
tur.pensize(1)
for i in range(36):
    tur.forward(100)
    tur.left(170)
    
tur.end_fill()

wn.mainloop()
