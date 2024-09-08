import turtle
import random
import re
from collections import defaultdict

def draw_tulip(t):
    t.speed(0)

    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("green")
    t.setheading(90)
    t.forward(100)

    t.left(30)
    t.color("green")
    t.begin_fill()
    t.circle(30, 90)
    t.left(90)
    t.circle(30, 90)
    t.end_fill()
    
    t.penup()
    t.goto(0, -30)
    t.setheading(0)
    t.pendown()
   
    t.color("red")
    for _ in range(3):
        t.begin_fill()
        t.circle(40, 60)
        t.left(120)
        t.circle(40, 60)
        t.end_fill()
        t.left(120)

    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


def draw_sunflower(t):
    t.speed(0)
    
    t.color("yellow")  
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    
    for _ in range(36):
        t.circle(70, 60)
        t.left(120)
        t.circle(70, 60)
        t.right(30)

def draw_rose(t):
    t.speed(0)
    t.color("red")  

    size = 25
    t.penup()
    t.setheading(0)
    t.pendown()

    for i in range(40):  
        t.circle(size, 100)  
        t.left(90)  
        t.circle(size, 100)
        t.left(60)  

def draw_daisy(t):
    t.speed(0)
    
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    t.color("white")  
    t.penup()
    t.left(90)
    t.forward(30)
    t.right(90)
    t.pendown()

    for _ in range(12):
        t.circle(60, 60)    
        t.left(120)
        t.circle(60, 60)
        t.right(30)

def draw_lily(t):
    t.speed(0)
    t.color("white")  
    
    for _ in range(6):
        t.begin_fill()
        t.circle(100, 60)  
        t.left(120)
        t.circle(100, 60)
        t.end_fill()
        t.left(60)

flower_types = ['sunflower', 'rose', 'daisy', 'tulip', 'lily']

def tokenize(sentence):
    number_words = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
        'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
    }

    info = defaultdict(lambda: None)

    match = re.search(r'\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b', sentence.lower())
    if match:
        num_flowers_str = match.group(0)
        if num_flowers_str.isdigit():
            info['num_flowers'] = int(float(num_flowers_str))
        else:
            info['num_flowers'] = number_words.get(num_flowers_str, 1)

    for flower in flower_types:
        if flower in sentence.lower():
            info['flower_type'] = flower
            break

    return info

def get_user_input():
    user_input = input(
        "Describe what you want (e.g., 'I want 3 sunflowers'): "
    )

    info = tokenize(user_input)

    num_flowers = info['num_flowers'] or 1  
    flower_type = info['flower_type'] or 'sunflower' 

    return num_flowers, flower_type

def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("white") 
    t = turtle.Turtle()
    t.speed(10)
    return t

def position_turtle(t):
    t.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    t.pendown()

def main():
    num_flowers, flower_type = get_user_input()

    flower_functions = {
        'sunflower': draw_sunflower,
        'rose': draw_rose,
        'daisy': draw_daisy,
        'tulip': draw_tulip,
        'lily': draw_lily
    }

    t = setup_turtle()

    for _ in range(num_flowers):
        position_turtle(t)
        flower_functions[flower_type](t)

    turtle.done()

if __name__ == "__main__":
    main()
