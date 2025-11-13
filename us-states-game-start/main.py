import turtle

import pandas
import pandas as pd

# Set up the game screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
correct_guesses = []  # list to store correctly guessed states

# Load all 50 states from the CSV
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()  # convert the 'state' column to a list

# Main game loop: runs until all 50 states are guessed
while len(correct_guesses) < 50:
    # Ask the player to guess a state
    answer_state = screen.textinput(
        title=f"Score: {score} / 50",
        prompt="What's another state's name?"
    ).title()  # ensure the first letter is capitalized for matching

    # If player types 'Exit', save the missing states and end the game
    if answer_state == "Exit":
        incorrect_guesses = [state for state in all_states if state not in correct_guesses]
        df = pd.DataFrame(incorrect_guesses)
        df.to_csv("states_to_learn.csv")  # save missing states to a CSV
        break

    # If the guessed state is valid and not already guessed
    if answer_state in states.state.values and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        data = states[states.state == answer_state]  # get row for that state
        x_data = data["x"].item()  # extract x coordinate
        y_data = data["y"].item()  # extract y coordinate

        # Create a new turtle to write the state's name on the map
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x_data, y_data)
        new_state.write(answer_state, align="center", font=("Arial", 8, "normal"))

        score += 1  # increase score for each correct guess
