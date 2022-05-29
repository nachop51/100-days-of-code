import turtle
import pandas
from print_message import PrintMessage

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")

message = PrintMessage()

game_is_on = True

counter = 0
correct_guesses = []
all_states = states.state.to_list()
while game_is_on:
    answer_state = screen.textinput(
        f"{counter}/50 States Correct", "What's another state's name?")

    answer_state = answer_state.title()

    if answer_state in "Exit":
        missing_states = [
            state for state in all_states if state not in correct_guesses]
        break
    elif answer_state in correct_guesses:
        continue
    elif answer_state in set(states["state"]):
        correct_guesses.append(answer_state)
        message.print_this(states[states.state == answer_state])
        counter += 1

df = pandas.DataFrame(missing_states)
df.to_csv("states_to_learn.csv")
