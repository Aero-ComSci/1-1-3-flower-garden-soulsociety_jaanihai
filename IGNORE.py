import turtle, random

def draw_sunflower(t):
    for _ in range(36):
        t.circle(50)
        t.right(10)

def draw_rose(t):
    for _ in range(5):
        t.circle(60, 180)
        t.left(144)

def draw_daisy(t):
    for _ in range(12):
        t.circle(40)
        t.left(30)

def draw_tulip(t):
    t.begin_fill()
    for _ in range(2):
        t.circle(40, 90)
        t.circle(40 // 2, 90)
    t.end_fill()

def draw_lily(t):
    for _ in range(5):
        t.circle(100, 60)
        t.left(144)

def get_user_input():
    flower_types = {
        '1': 'sunflower',
        '2': 'rose',
        '3': 'daisy',
        '4': 'tulip',
        '5': 'lily'
    }

    num_flowers = int(input("How many flowers would you like to draw? "))

    print("Choose a type of flower:")
    print("1. Sunflower")
    print("2. Rose")
    print("3. Daisy")
    print("4. Tulip")
    print("5. Lily")
    flower_choice = input("Enter the number corresponding to the flower: ")

    return num_flowers, flower_types[flower_choice]

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
    t = setup_turtle()
    num_flowers, flower_type = get_user_input()

    flower_functions = {
        'sunflower': draw_sunflower,
        'rose': draw_rose,
        'daisy': draw_daisy,
        'tulip': draw_tulip,
        'lily': draw_lily
    }

    for _ in range(num_flowers):
        position_turtle(t)
        flower_functions[flower_type](t)

    turtle.done()

if __name__ == "__main__":
    main()



