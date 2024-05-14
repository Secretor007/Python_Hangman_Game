import random
import hangmanwords
from hangmanui import stages, logo

print(logo)
lives = 6
chosen_word = random.choice(hangmanwords.word_list)
chosen_word = list(chosen_word)
word_length = len(stages) - 1
display = []

for letter in range(len(chosen_word)):
    display.append("_")
#mouse=5
print(display)
while display != chosen_word and lives > 0:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if guess in display:
        print(f"Your letter {guess} is already present.")
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
    if guess not in display:
        print(f"Your letter {guess} is not present in the secret word.Please type different letter.")
        lives = lives - 1
        print(stages[word_length - 1])
        word_length -= 1
        if lives != 0:
            print(f"You have left {lives} lives.")

if "_" not in display:
    print("You Win")
if lives == 0:
    print("You Lose")

################HANGMAN###############
# import random
# word_list = ["ardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)


# display = []
# display_str=''

# for letter in range(len(chosen_word)):
#         display.append("_")
#     #mouse=5
# for ele in display:
#      display_str+=ele
# print(display_str)
# while display_str!=chosen_word:
#     guess = input("Guess a letter: ")
#     guess = guess.lower()
#     for i in range(len(chosen_word)):
#         if chosen_word[i]==guess:
#             display[i]=guess
#     print(display)


# for char in chosen_word:
# if char == guess:
#     print("True")
# else:
#     print("False")


# for name in chosen_word:
# if chosen_word.__contains__(guess)==True:
#     print("True")
# elif chosen_word.__contains__(guess)==False :
#     print("False")
