import turtle

bob = turtle.Turtle()


bob.color('#000000', '#FFFACD')
bob.pensize(5)
bob.penup()
bob.goto(-100,-50)
bob.pendown()
bob.right(105)
bob.begin_fill()
bob.circle(500,-30)
bob.circle(70,-30)
bob.right(105)
bob.circle(500,-30)
bob.end_fill()
bob.color('#000000', '#FFFF00')
bob.begin_fill()
bob.right(195)
bob.forward(25)
bob.backward(25)
bob.circle(70,-90)
bob.right(15)
bob.circle(300,-25)
bob.circle(90,60)
bob.circle(90,60)
bob.right(15)
bob.forward(25)
bob.right(125)
bob.circle(500,-30)
bob.right(130)
bob.circle(500,-30)
bob.right(80)
bob.circle(135,80)
bob.circle(300,-40)
bob.right(25)
bob.circle(70,-70)
bob.end_fill()
bob.color('#000000', '#FFFACD')
bob.pensize(5)
bob.penup()
bob.right(175)
bob.begin_fill()
bob.circle(30,-210)
bob.end_fill()


turtle.done()