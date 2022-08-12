# The game is suppose about the computer generating a random number between 1 - 100 and the user trys to guess what number it is
import random


random_ranked_number = random.randint(1, 10)

# print(random_ranked_number)

clues_for_multiples_of_10_2 = [
    "The number is even", "The number is a multiple of 2"]

clues_for_multiples_of_odd = ["The number is an odd number"]

multiples_of_10 = ["The number is a multiple of 10"]

multiples_of_3_5 = ("The number is a multiply of 3",
                    "The number is a multiply of 5")


def set_clues_for_user(random_number):
    if random_number % 2 == 0 and random_number % 10 == 0:
        random_index = random.randrange(0, 10)
        return f"{clues_for_multiples_of_10_2[random_index]} \n {multiples_of_10[0]}"
    if random_number % 3 == 0 and random_number % 10 == 0:
        return f"{multiples_of_3_5[0]} \n {multiples_of_10[0]}"
    if random_number % 5 == 0 and random_number % 10 == 0:
        return f"{multiples_of_3_5[1]} \n {multiples_of_10[0]}"
    if random_number % 3 == 0 and random_number % 5 == 0:
        return f"{multiples_of_3_5[0]} \n {multiples_of_3_5[1]}"
    if random_number % 10 == 0:
        return multiples_of_10[0]
    if random_number % 2 == 0:
        random_index = random.randint(0, len(clues_for_multiples_of_10_2) - 1)
        return clues_for_multiples_of_10_2[random_index]
    if random_number % 3 == 0:
        return multiples_of_3_5[0]
    if random_number % 5 == 0:
        return multiples_of_3_5[1]
    return "The number is a prime number"


print("=> ", set_clues_for_user(random_ranked_number))


def compare_user_input(random_number, user_input):
    if random_number == int(user_input):
        print("yay🤩🎆 you did it")
    else:
        print("Wrong guess try again")
        play_mini_game()


def play_mini_game():
    get_user_input = input("Guess a number between 1 and 10: ")
    print(f"You picked {get_user_input}")
    print("=> ", set_clues_for_user(random_ranked_number))
    compare_user_input(random_ranked_number, get_user_input)


print(play_mini_game())
