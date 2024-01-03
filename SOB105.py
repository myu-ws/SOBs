from turtle import *

def branch(l, w):
    if l < 8:
        return
    
    elif l > 10:
        pensize(w)
        forward(l)
        fruit(3, 3, "violet")
        fruit(2, 2, "yellow")
        left(30)
        color("chocolate")
        branch(4*l/5, 1)
        right(60)
        branch(4*l/5, 1)
        left(30)
        backward(l)
        
def fruit(s, r, c):
    pensize(s)
    color(c) 
    circle(r)
  
def main():
    window = Screen()
    window.setup(800,600)
    window.bgcolor("black")
    speed(0)
    penup()
    goto(0, -200)
    pendown()
    color("chocolate")
    left(90)
    branch(100, 2)
  
    window.exitonclick()
  
if __name__ == "__main__":
    main()

