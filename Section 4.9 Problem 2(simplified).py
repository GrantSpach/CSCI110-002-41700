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
    for i in range(1):
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.penup()
        t.backward(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()



wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Multi Square")


grant = turtle.Turtle()
grant.speed(2)
grant.color("red")
grant.pensize(3)
draw_square(grant, 20)
draw_square(grant, 40)
draw_square(grant, 60)
draw_square(grant, 80)
draw_square(grant, 100)



wn.mainloop()