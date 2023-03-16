import turtle
import pandas
state_name = []
x = []
y = []


# To Get the Co ordinate of x and y on mouse click.
def get_mouse_click_coor(x1, y1):
    global name
    name = screen.textinput(prompt="What's the another state's name.", title="Guess the State.").title()
    state_name.append(name)
    x.append(x1)
    y.append(y1)
    print(x1, y1, name)


screen = turtle.Screen()
screen.title("INDIA STATE GAME.")
image = "india_state.gif"
screen.addshape(image)
turtle.shape(image)
name = screen.textinput(prompt="What's the another state's name.", title="Guess the State.").title()

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

states_dict = {
    "state": state_name,
    "x": x,
    "y": y,
}
print(states_dict)
file = pandas.DataFrame(states_dict)
file.to_csv("states_of_India.csv")
