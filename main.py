import random
import hangman
user_lifes = 6
password = hangman.words[random.randint(0, 63)]
hangman_index = 0
password_guess = len(password)


def printHangman(index):
    print(hangman.HANGMANPICS[index])
    print(" ")

print(" ")
print("Welcome to hangman game!")
printHangman(0)

while user_lifes > 0 and password_guess != 0:
    user_guess = input("Guess a letter (category animals): ")
    if user_guess not in password:
        user_lifes -= 1
        hangman_index += 1
        printHangman(hangman_index)
    else:
        printHangman(hangman_index)
        password_guess -= 1

if user_lifes == 0:
    print(hangman.HANGMANPICS[-1])
    print(" ")
    print("You lost!")
    print(f"The password was: {password}")

if user_lifes > 0 and password_guess == 0:
    printHangman(hangman_index)
    print("You won!")