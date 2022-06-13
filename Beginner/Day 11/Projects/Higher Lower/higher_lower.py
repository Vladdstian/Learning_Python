# This program is a guessing game where you have to guess which person has more followers on Instagram
import game_data
import random
import game_art


def game_start():
    game_score = 0
    guess = True
    while guess:
        # randomise guessing choices
        first_person = random.randint(0, len(game_data.data) - 1)
        second_person = random.randint(0, len(game_data.data) - 1)
        while first_person == second_person:
            second_person = random.randint(0, len(game_data.data) - 1)
        f_p_name = game_data.data[first_person]['name']
        f_p_follower_count = game_data.data[first_person]['follower_count']
        f_p_description = game_data.data[first_person]['description']
        f_p_country = game_data.data[first_person]['country']

        s_p_name = game_data.data[second_person]['name']
        s_p_follower_count = game_data.data[second_person]['follower_count']
        s_p_description = game_data.data[second_person]['description']
        s_p_country = game_data.data[second_person]['country']

        # Game start
        print(game_art.logo)
        print(f"Compare A: {f_p_name}, {f_p_description}, {f_p_country}")
        print(game_art.vs)
        print(f"Against B: {s_p_name}, {s_p_description}, {s_p_country}")

        # check for validation
        guess = input("Who has more followers? Type 'A' of 'B'\n")
        if guess == 'A' and f_p_follower_count > s_p_follower_count:
            game_score += 1
            print(f"You're right! Current score: {game_score}")
            continue
        elif guess == 'B' and f_p_follower_count < s_p_follower_count:
            game_score += 1
            print(f"You're right! Current score: {game_score}")
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {game_score}")
            game_score = 0
            game_start()


game_start()
