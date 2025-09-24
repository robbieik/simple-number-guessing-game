import random
import os
import json

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def load_save_data():
    if os.path.exists("savegame.json"):
        try:
            with open("savegame.json", "r") as f:
                return json.load(f)
        except:
            return create_default_save()
    else:
        return create_default_save()
    
def create_default_save():
    return {
        "player_stats": {
            "highscore": 0,
            "games_played": 0,
            "total_attempts": 0
        },
        "achievements": []
    }

def save_data(data):
    try:
        with open("savegame.json", "w") as f:
            json.dump(data, f, indent=2)
        return True
    except:
        print("Error saving game data.")
        return False

def update_stats(save_data, attempts):
    stats = save_data["player_stats"]
    stats["games_played"] += 1
    stats["total_attempts"] += attempts
    if stats["highscore"] == 0 or attempts < stats["highscore"]:
        stats["highscore"] = attempts
        return True #NEW HIGHSCORE
    return False

def give_hint(hint_prompt):
    digits = 0
    guess = number_to_guess
    global received_hints
    global penalty
    if hint_prompt.lower() == "yes":
        if received_hints < 4:
            received_hints += 1
            penalty += 1
            if attempts < 3:
                if number_to_guess % 2 == 0:
                    print("Hint: The number is even.")
                else:
                    print("Hint: The number is odd.")
            elif 3 <= attempts < 6:
                while guess > 0:
                    digits += 1
                    guess //= 10
                print(f"Hint: The number has {digits} digits.")
            elif 6 <= attempts < 9:
                if number_to_guess % 2 == 0 and number_to_guess % 3 == 0:
                    print("Hint: The number is divisible by 2 and 3.")
                elif number_to_guess % 3 == 0:
                    print("Hint: The number is divisible by 3.")
                elif number_to_guess % 5 == 0:
                    print("Hint: The number is divisible by 5.")
                elif is_prime(number_to_guess):
                    print("Hint: The number is a prime number.")
            elif attempts >= 9:
                percentage = random.randint(10, 30)
                hint_lower_limit = int(number_to_guess - percentage / 100 * number_to_guess)
                percentage = random.randint(10, 30)
                hint_upper_limit = int(number_to_guess + percentage / 100 * number_to_guess)
                if hint_lower_limit < lower_limit:
                    print(f"Hint: The number is between {lower_limit} and {hint_upper_limit}.")
                elif hint_upper_limit > upper_limit:
                    print(f"Hint: The number is between {hint_lower_limit} and {upper_limit}.")
                else:
                    print(f"Hint: The number is between {hint_lower_limit} and {hint_upper_limit}.")
                penalty += 3
                print("Note: An additional 3 penalty points have been added for this hint.")
        else:
            print("You have used all your hints for this round.")
    else:
        print("No hint will be provided.")
    hint_prompt = ""

def choose_difficulty():
    global difficulty
    difficulty = input ("Please choose your difficulty level\n1. very easy\n2. easy\n3. medium\n4. hard\n5. extreme\n6. Are you insane?\n7. custom\nTo choose the level, please input the option number:")
    global lower_limit
    global upper_limit
    difficulty_levels = {
        "1": (1, 10),
        "2": (1, 100),
        "3": (1, 1000),
        "4": (1, 10000),
        "5": (1, 100000),
        "6": (1, 1000000)
    }
    if difficulty in difficulty_levels:
        lower_limit, upper_limit = difficulty_levels[difficulty]
        print(f"You have chosen level {difficulty} with a range from {lower_limit} to {upper_limit}.")
    elif difficulty == "7":
        lower_limit = int(input("Please enter the lower limit of your desired range(should be a number): "))
        upper_limit = int(input("Please enter the upper limit of your desired range(should be a number): "))
        if lower_limit >= upper_limit:
            print("Invalid range. The lower limit must be less than the upper limit. Setting to default range 1 to 100.")
            lower_limit, upper_limit = 1, 100
        else:
            print(f"You have chosen a custom range from {lower_limit} to {upper_limit}.")

response = "yes"
highscore = 0
game_data = load_save_data()
if game_data["player_stats"]["games_played"] > 0:
    highscore = game_data["player_stats"]["highscore"]
    print(f"Welcome back! Games played: {game_data['player_stats']['games_played']}")
    print(f"Your best score so far is {highscore} attempts.")
else:
    print("Welcome to the Number Guessing Game! Let's set a high score!")
while response.lower() == "yes":
    choose_difficulty()
    attempts = 0
    penalty = 0
    highscore = game_data["player_stats"]["highscore"]
    guessed = False
    number_to_guess = random.randint(lower_limit, upper_limit)
    received_hints = 0
    print(f"The number between {lower_limit} and {upper_limit} has been generated.")
    while guessed == False:
        number = input("Please enter your guess: ")
        if number.isdigit():
            number = int(number)
            attempts += 1
            if number < number_to_guess:
                print("Too low! Try again.")
            elif number > number_to_guess:
                print("Too high! Try again.")
            elif number == number_to_guess:
                print(f"Congratulations! You have guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
                if penalty > 0:
                    print(f"Note: You received {penalty} penalty points for using hints.")
                    attempts += penalty
                    print(f"Your total points including penalties is {attempts}.")
                new_record = update_stats(game_data, attempts)
                if save_data(game_data):
                    if new_record:
                        print(f"New all-time best score: {attempts} points.")
                    else:
                        print(f"All-time best score remains: {game_data['player_stats']['highscore']} points.")
            if attempts in [2,5,8,11] and not guessed and difficulty != "1":
                hint_prompt = input("Would you like a hint (This will add 1 to your attempts number)? (yes/no): ")
                give_hint(hint_prompt)
        else:
            print("Invalid input. Please enter a valid number.")
    response = input("Do you want to play again? (yes/no): ")
print(f"Thank you for playing! In this session, your best score was {game_data['player_stats']['highscore']} points.")
