import random
import time

print("Welcome to guessing game\n")             #Game Invitation
name = input("Enter your name: ")
print("Hello " + name + " Best of luck for your game!!!")
time.sleep(2)
print("Let's begin !!!")
print("Let's play game! Hoorayyy !!!")
time.sleep(3)

def main():                                     #Compulsations for game
    global count
    global display
    global words
    global guessed
    global length
    global play_game
    guessing_words = ["january", "border", "february", "ball", "ballon", "keys", "ear", "yolk", "fork", "plants"]
    print(guessing_words)
    words =random.choice(guessing_words)
    length = len(words)
    count = 0
    display = '_' * length
    guessed = []
    play_game = ""

def loop_play():                                #First executing Loop
    global play_game
    play_game =input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thanks for playing! We will be looking forward to you!!")
            exit()

def game():                                     # Compulsary conditions for the game
    global count
    global display
    global words
    global guessed
    global length
    global play_game
    limit = 5
    print("This is guessing word: " + display)
    guessing = input("Enter your guess: ")
    guessing = guessing.strip()
    if len(guessing.strip()) == 0 or len(guessing.strip()) >= 2 or guessing <= "10":
        print("Invalid Input, Try a letter\n")
        game()
    elif guessing in words:
        guessed.extend([guessing])
        label = words.find(guessing)
        words =words[:label] + "_" + words[label + 1:]
        display =display[:label] + guessing + display[label + 1:]
        print(display + '\n')
    elif guessing in guessed:
        print("Please Try another letter. Choose wisely !!! \n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("  -------\n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("__|____  \n")
            print("Bad Guess " + str(limit - count) + " remaining guesses\n")
        elif count == 2:
            time.sleep(1)
            print("  -------\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("__|____  \n")
            print("Bad Guess " + str(limit - count) + " remaining guesses\n")
        elif count == 3:
            time.sleep(1)
            print("  -------\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("__|____  \n")
            print("Bad Guess " + str(limit - count) + " remaining guesses\n")
        elif count == 4:
            time.sleep(1)
            print("  -------\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     |\n")
            print("  |     0 \n")
            print("  |      \n")
            print("  |      \n")
            print("  |      \n")
            print("__|____  \n")
            print("Bad Guess " + str(limit - count) + " remaining guess. It is your last guess.\n")
        elif count == 5:
            time.sleep(1)
            print("  ------- \n")
            print("  |     | \n")
            print("  |     | \n")
            print("  |     | \n")
            print("  |     | \n")
            print("  |     0  \n")
            print("  |    /|\ \n")
            print("  |    / \ \n")
            print("  |      \n")
            print("__|____  \n")
            print("Bad Guess " + str(limit - count) + " Tada Tata bye bye Meet you later!!!\n")
            print("Word was: ", guessed, words)
            loop_play()
    if words == '_' * length:
        print("Congratulations!! Your guess was right!!")
        loop_play()
    elif count!= limit:
        game()

main()
game()