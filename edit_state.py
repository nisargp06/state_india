import turtle
import pandas


def get_mouse_click_coor(x1, y1):
    # global name
    name = screen.textinput(prompt="What's the another state's name.", title="Guess the State.").title()
    data = pandas.read_csv("states_of_India.csv")
    file = data[data.state == name]
    print(file)
    print
    file["x"] = x1
    # file.y = str(y1)
    # state_name.append(name)
    # x.append(x1)
    # y.append(y1)
    print(x1, y1, name)


screen = turtle.Screen()
screen.title("INDIA STATE GAME.")
image = "india_state.gif"
screen.addshape(image)
turtle.shape(image)
# name = screen.textinput(prompt="What's the another state's name.", title="Guess the State.").title()
# guessed_state = []
# while len(guessed_state) < 50:
#     screen.textinput(prompt="What's the another state's name.", title="Guess the State.").title()

# data = pandas.read_csv("states_of_India.csv")
# file = data[data.state == name]
# print(file)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()