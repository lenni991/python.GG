import random
from replit import clear

def print_welcome_message():
    print('\nWelcome to the number guessing game!')

def compare_numbers(guessed_number, target_number):
    difference = guessed_number - target_number
    absolute_difference = abs(difference)

    if absolute_difference == 0:
        print(f"Well Played! You guessed the exact number: {target_number}")
    elif absolute_difference <= 2:
        print("Very close! You are almost there.")
    elif absolute_difference <= 5:
        if difference < 0:
            print("Try a slightly lower number.")
        else:
            print("Try a slightly higher number.")
    else:
        if difference < 0:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

def play_game():
    target_number = random.randint(1, 100)
    print('I\'m thinking of a number between 1 and 100')

    attempts = 10 if input('Choose difficulty - [easy] or [hard]: ').lower() == 'easy' else 5

    for attempt in range(attempts):
        guess = int(input('Make a guess: '))
        compare_numbers(guess, target_number)
        
        if guess == target_number:
            break
    else:
        print(f"\nSorry, you've run out of attempts. The number I was thinking of was: {target_number}")

def main():
    print_welcome_message()

    while True:
        if input('\nDo you want to play (y/n)? ').lower() != 'y':
            print('Thanks for playing! Goodbye!')
            break
        clear()
        play_game()

if __name__ == "__main__":
    main()
