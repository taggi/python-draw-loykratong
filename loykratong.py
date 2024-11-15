import turtle as t
t.speed(0)
t.width(5)
t.setup(width=1200, height=1200, startx=0, starty=0)
t.Screen().bgcolor('#f7f7f7')

# Banana leaf
def leaf(fcolor="orange"):
    t.fillcolor(fcolor)
    t.begin_fill()
    t.right(120)        
    t.forward(100)      
    t.circle(60, 240)   
    t.forward(100)
    t.end_fill()

#Candle
def candle(fcolor="green"):
    t.fillcolor(fcolor)
    t.begin_fill()
    t.right(120)        
    t.forward(50)      
    t.circle(30, 240)   
    t.forward(50)
    t.end_fill()


# candle
t.penup()
t.color('#f5b95b')
t.goto(-80,-110)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(290)
t.left(90)
t.forward(20)
t.left(90)
t.forward(290)
t.left(90)
t.forward(20)
t.end_fill()
t.penup()
t.goto(-90, 260)
candle("#e9968c") 
t.color('#f7d881')
t.pensize(20)
t.goto(-40, 260)
t.setheading(45)
t.pendown()
t.forward(40)
t.penup()
t.goto(-90, 280)
t.pendown()
t.setheading(90)
t.forward(40)
t.penup()
t.goto(-160, 285)
t.setheading(-45)
t.pendown()
t.forward(40)

#Incense
t.penup()
t.goto(40, -100)
t.setheading(90)
t.color('#a0a8b2')
t.pensize(15)
t.pendown()
t.forward(500)
t.penup()
t.right(90)
t.forward(30)
t.pendown()
t.right(90)
t.forward(500)

# Body
t.penup()
t.color('#cda57d')
t.goto(-350,-110)
t.setheading(0)
t.pensize(1)
t.pendown()
t.begin_fill()
t.forward(650)
t.right(90)
t.forward(80)
t.right(90)
t.forward(568)
t.forward(80)
t.right(90)
t.forward(80)
t.end_fill()
t.penup()

# Lotus
t.penup()
t.setposition(-250,60)
t.setheading(0)
t.pendown()
leaf("#78b75b")
t.penup()
t.right(120)
t.forward(110)
leaf("#78b75b")
t.penup()
t.right(120)
t.forward(110)
leaf("#78b75b")
t.penup()
t.right(120)
t.forward(110)
leaf("#78b75b")
t.penup()
t.right(120)
t.forward(110)
leaf("#78b75b")


#water
t.penup()
t.setposition(-1000,-180)
t.setheading(0)
t.pendown()
t.color("#8bd2f5")
t.begin_fill()
t.forward(2200)
t.right(90)
t.forward(600)
t.right(90)
t.forward(2200)
t.right(90)
t.forward(600)
t.end_fill()
t.penup()

#Moon
t.goto(300, 400)
t.color('#f5cf74')
t.dot(150)

#Text
t.color("#f2c351")
t.penup()
t.goto(-400, 400)
t.pendown()
style = ('Stencil Std Bold',32,'bold')
t.write('สวัสดีวันลอยกระทง 2567',font=style,move=True)


t.hideturtle()      
t.done()
