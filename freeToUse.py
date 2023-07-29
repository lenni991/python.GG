def compare_numbers(n1, n2):
    difference = n1 - n2
    absolute_difference = abs(difference)

    if absolute_difference == 0:
        print("Congratulations! You guessed the exact number:", n2)
    elif absolute_difference <= 2:
        print("Very close! You are almost there.")
    elif absolute_difference <= 5:
        if difference < 0:
            print("Getting warmer! Try a slightly lower number.")
        else:
            print("Getting warmer! Try a slightly higher number.")
    else:
        if difference < 0:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
