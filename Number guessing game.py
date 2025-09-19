import random

response = "yes"
highscore = 0
while response.lower() == "yes":
    lower_limit = input("Please enter the lower limit of your desired range: ")
    upper_limit = input("Please enter the upper limit of your desired range: ")
    if lower_limit.isdigit() and upper_limit.isdigit():
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        if lower_limit < upper_limit:
            attempts = 0
            guessed = False
            number_to_guess = random.randint(lower_limit, upper_limit)
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
                        if highscore == 0 or highscore > attempts:
                            highscore = int(attempts)
                            print(f"New best score: {highscore} attempts.")
                        else:
                            print(f"Best score remains: {highscore} attempts.")
                else:
                    print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid range. The lower limit must be less than the upper limit.")
    else:
        print("Invalid input. Please enter valid numbers for the limits.")
    response = input("Do you want to play again? (yes/no): ")
print(f"Thank you for playing! In this session, your best score was {highscore} attempts.")