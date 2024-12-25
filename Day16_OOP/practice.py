# Turtle과 Screen은 파스칼 케이스로 선언된 Class임
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()