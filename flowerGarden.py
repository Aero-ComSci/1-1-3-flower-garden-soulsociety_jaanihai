import turtle
import random
import re
from collections import defaultdict


def draw_sunflower(t):
    t.speed(0)
    
    t.color(flower_color)
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
    t.color(flower_color)
    
    t.penup()
    t.setheading(0)
    t.pendown()
    
    for i in range(50):
        t.circle(i * 2, 60) 
        t.left(60)


def draw_daisy(t):
    t.speed(0)
    
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    t.color(flower_color)
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


def draw_tulip(t):
    t.speed(0)
    t.color(flower_color)
    
    
    t.begin_fill()
    t.circle(40, 180)  
    t.left(90)
    
    for _ in range(2):
        t.circle(40, 90)
        t.left(90)
    t.end_fill()


def draw_lily(t):
    t.speed(0)
    t.color(flower_color)
    
    for _ in range(6):
        t.begin_fill()
        t.circle(100, 60)  
        t.left(120)
        t.circle(100, 60)
        t.end_fill()
        t.left(60)


flower_types = ['sunflower', 'rose', 'daisy', 'tulip', 'lily']
colors = ['red', 'yellow', 'blue', 'green', 'white', 'purple', 'orange', 'pink', 'black']

def extract_info(sentence):
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

    for color in colors:
        if color in sentence.lower():
            info['flower_color'] = color
            break

    for color in colors:
        if f"background {color}" in sentence.lower():
            info['bg_color'] = color
            break

    return info

def get_user_input():
    user_input = input(
        "Describe what you want (e.g., 'I want 3 yellow sunflowers'): "
    )

    info = extract_info(user_input)

    num_flowers = info['num_flowers'] or 1  
    flower_type = info['flower_type'] or 'sunflower' 
    global flower_color
    flower_color = info['flower_color'] or 'yellow' 
    bg_color = info['bg_color'] or 'white'  

    return num_flowers, flower_type, flower_color, bg_color

def setup_turtle(bg_color):
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
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
    global flower_color
    num_flowers, flower_type, flower_color, bg_color = get_user_input()

    flower_functions = {
        'sunflower': draw_sunflower,
        'rose': draw_rose,
        'daisy': draw_daisy,
        'tulip': draw_tulip,
        'lily': draw_lily
    }

    t = setup_turtle(bg_color)

    for _ in range(num_flowers):
        position_turtle(t)
        flower_functions[flower_type](t)

    turtle.done()

if __name__ == "__main__":
    main()
