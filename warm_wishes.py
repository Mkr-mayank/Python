# import turtle
# pen=turtle.Turtle()
# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)
# def heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curve()
#     pen.left(120)
#     curve()
#     pen.forward(112)
#     pen.end_fill()
# def txt():
#     pen.up()
#     pen.setpos(-50,95)
#     pen.down()
#     pen.color('white')
#     pen.write("Happy Birthday ", font=("Forte",16))
# heart()
# txt()
# pen.ht()
# turtle
# turtle.exitonclick()

# Importing turtle library to draw "Happy Birthday"
import turtle

# Creating our turtle cursor to draw
my_turtle_cursor = turtle.Turtle()

# Creating a separate Canvas to draw "Happy Birthday"
my_turtle_screen = turtle.Screen()

# initializing a variable for co-ordinating
y_coordinate = -125

my_turtle_cursor.speed(25)
# Creating a function to draw a circle on top of stick
def draw_circle_on_top_of_stick(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)
    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor('lavender')

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    my_turtle_cursor.circle(radius)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

def draw_candle_for_cake(fill_color, border_color, x, y):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)

    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing the first side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the second side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    # Drawing the third side of our Candle
    my_turtle_cursor.forward(25)
    my_turtle_cursor.left(90)

    # Drawing the fourth side of our Candle
    my_turtle_cursor.forward(60)
    my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()

    my_turtle_cursor.getscreen().update()

# Creating a Function to draw stick on the candle
def draw_stick_on_candle(fill_color, x, y, cursor_size):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(fill_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pensize(cursor_size)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.right(90)
    my_turtle_cursor.forward(12)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

def write_happy_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("Happy", font=("Calisto MT", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def write_birthday_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()

    my_turtle_cursor.write("Birthday", font=("Calisto MT", 26, "bold"))

    my_turtle_cursor.getscreen().update()

def write_your_name_inside_circle(text_color, x, y):
    my_turtle_cursor.penup()
    # Changing color of our cursor
    my_turtle_cursor.color(text_color)

    # Changing fill color of the cursor
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.color('blue')
    my_turtle_cursor.write("Aeishika Mam", font=("Monotype Corsiva", 18, "bold italic"))

    my_turtle_cursor.getscreen().update()
def draw_stick(fill_color, border_color, x, y):
    my_turtle_cursor.penup()
    my_turtle_cursor.pensize(3)

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.pendown()
    my_turtle_cursor.left(180)
    my_turtle_cursor.forward(170)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Function to draw topping of our cake
def draw_toppings_on_cake(fill_color, border_color, x, y, radius):
    my_turtle_cursor.penup()

    # Changing color of our cursor
    my_turtle_cursor.color(border_color)

    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()
    my_turtle_cursor.begin_fill()

    # Drawing a circle using circle function
    my_turtle_cursor.forward(10)
    my_turtle_cursor.left(90)
    my_turtle_cursor.circle(radius, extent = 180)
    my_turtle_cursor.left(90)
    my_turtle_cursor.forward(10)
    my_turtle_cursor.end_fill()
    my_turtle_cursor.getscreen().update()

# Creating a Function to draw different layers of a cake
def draw_layer_of_the_cake(fill_color, border_color, cursor_size, x, y, width, height):
    my_turtle_cursor.hideturtle()
    my_turtle_cursor.penup()

    my_turtle_cursor.pensize(cursor_size)
    # Changing color of our cursor
    my_turtle_cursor.color(border_color)
    # Changing fill color of the cursor
    my_turtle_cursor.fillcolor(fill_color)
    my_turtle_cursor.goto(x, y)
    my_turtle_cursor.pendown()

    # Starting the cursor to fill color
    my_turtle_cursor.begin_fill()

    for i in range(2):
        my_turtle_cursor.forward(width)
        my_turtle_cursor.left(90)
        my_turtle_cursor.forward(height)
        my_turtle_cursor.left(90)

    my_turtle_cursor.end_fill()
    my_turtle_cursor.setheading(0)
    my_turtle_cursor.getscreen().update()

# Changing the background color of our canvas
my_turtle_screen.bgcolor("#FFFDD0")

# # Creating an empty list of different parts of our cake
parts_of_cake = []
parts_of_cake.append(["#854B4A", "#000000", 3, 30])
parts_of_cake.append(["#FFFDF7", "#000000", 3, 20])
parts_of_cake.append(["#FF5DB3", "#000000", 3, 60])

# drawing an plate for our cake using draw_layer_of_the_cake() function
draw_layer_of_the_cake("#07006B", "#000000", 3, -220, y_coordinate - 70, 400, 10)

# Drawing different parts of our cake
for parts in parts_of_cake:
    draw_layer_of_the_cake(parts[0], parts[1], parts[2], -135, y_coordinate - 60, 240, parts[3])
    y_coordinate += parts[3]


# drawing top topping of our cake
draw_toppings_on_cake("#C20067", "#000000", -120, y_coordinate - 60, 10)
draw_toppings_on_cake("#FFFF00", "#000000", -80, y_coordinate - 60, 10)
draw_toppings_on_cake("#FF0000", "#000000", 25, y_coordinate - 60, 10)
draw_toppings_on_cake("#0000FF", "#000000", 59, y_coordinate - 60, 10)

# drawing middle topping of our cakes
draw_toppings_on_cake("#FF0101", "#000000", -135, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -135, y_coordinate - 100, 10)
draw_toppings_on_cake("#18DEE8", "#000000", -135, y_coordinate - 120, 10)
draw_toppings_on_cake("#00CC17", "#000000", -80, y_coordinate - 80, 10)
draw_toppings_on_cake("#0000FF", "#000000", -65, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", -95, y_coordinate - 140, 10)
draw_toppings_on_cake("#8130B8", "#000000", 10, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", -20, y_coordinate - 110, 10)
draw_toppings_on_cake("#E824D2", "#000000", 35, y_coordinate - 140, 10)
draw_toppings_on_cake("#FFA500", "#000000", 75, y_coordinate - 80, 10)
draw_toppings_on_cake("#E4E6EB", "#000000", 75, y_coordinate - 110, 10)
draw_toppings_on_cake("#FFD700", "#000000", 75, y_coordinate - 140, 10)

# Drawing candle on of our cake using draw_candle_for_cake() function
draw_candle_for_cake("#FFF44F", "#000000", -40, y_coordinate - 60)

# Drawing stick on top og uou candle
draw_stick_on_candle("#181A18", -26, y_coordinate + 15, 7)

# Drawing a stick for writing Happy Birthday
draw_stick("#181A18", "#181A18", 0, y_coordinate - 60)

# Drawing a circle on top of stick
draw_circle_on_top_of_stick("#F5CCFF", "#FFFDD0", 90, y_coordinate + 200, 90)

# Writing "Happy" inside of our circle
write_happy_inside_circle("#000000", -50, y_coordinate + 240)

# Writing "Birthday" inside of our circle
write_birthday_inside_circle("#000000", -65, y_coordinate + 200)

# Writing "Name" inside of our circle
write_your_name_inside_circle("#000000", -70, y_coordinate +160)
# Calling done function at the end
turtle.done()