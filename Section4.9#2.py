#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      grant
#
# Created:     05/03/2025
# Copyright:   (c) grant 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



import turtle

def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Multi Square")


grant = turtle.Turtle()
grant.speed(2)
grant.color("red")
grant.pensize(3)
draw_square(grant, 20)
grant.penup()
grant.backward(10)
grant.right(90)
grant.forward(10)
grant.left(90)
grant.pendown()
draw_square(grant, 40)
grant.penup()
grant.backward(10)
grant.right(90)
grant.forward(10)
grant.left(90)
grant.pendown()
draw_square(grant, 60)
grant.penup()
grant.backward(10)
grant.right(90)
grant.forward(10)
grant.left(90)
grant.pendown()
draw_square(grant, 80)
grant.penup()
grant.backward(10)
grant.right(90)
grant.forward(10)
grant.left(90)
grant.pendown()
draw_square(grant, 100)



wn.mainloop()