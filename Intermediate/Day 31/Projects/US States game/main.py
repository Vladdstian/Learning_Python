import turtle
import pandas

IMAGE_STATES = "blank_states_img.gif"

states_data = pandas.read_csv("50_states.csv")
all_states = states_data["state"].to_list()
print(all_states)
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE_STATES)
turtle.shape(IMAGE_STATES)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

while len(guessed_states) != 50:
    state_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="Please enter the name of a state: ").title()
    if state_guess == "Exit":
        # CHANGED this If statement and use a list comprehension
        missing_states = [n for n in all_states if n not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if state_guess in all_states:
        if state_guess not in guessed_states:
            state = states_data[states_data.state == state_guess]
            new_x = int(state.x)
            new_y = int(state.y)
            pen.goto(x=new_x, y=new_y)
            pen.write(state_guess)
            guessed_states.append(state_guess)

screen.textinput(title="Congratulations!", prompt=f"You have guessed {len(guessed_states)} states!")
turtle.mainloop()
