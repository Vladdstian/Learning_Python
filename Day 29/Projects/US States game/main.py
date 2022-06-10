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
# screen.bgpic(IMAGE_STATES)
turtle.shape(IMAGE_STATES)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

# Function used to take all the input from mouse click and show the coordinates -
# used to get the coord from the pictures
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

while len(guessed_states) != 50:
    state_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="Please enter the name of a state: ").title()
    if state_guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
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
