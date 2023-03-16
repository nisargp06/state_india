import turtle
import pandas
FONT = ("Courier", 8, "normal")

score = 0
tim = turtle.Turtle()
tim.color("red")
tim.penup()
tim.hideturtle()
screen = turtle.Screen()
screen.title("INDIA STATE GAME.")
image = "india_state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states_of_India.csv")
all_states = data.state.to_list()
print(type(all_states))

guessed_state = []

while len(guessed_state) < 32:
    answer_state = screen.textinput(prompt=f"What's the another state's name.{score}/{len(all_states)}\nenter exit to quit", title="Guess the State.").title()
    if answer_state == "Exit":
        missing_state = [n for n in all_states if n not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            score += 1
            print(answer_state)
            state = data[data.state == answer_state]
            tim.goto(x=int(state.x), y=int(state.y))
            tim.write(answer_state, font=FONT)




