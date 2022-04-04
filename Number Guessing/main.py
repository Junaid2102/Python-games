import random
#print(number)        // We use it for printing the random number can say it is a cheat code.
name = input("Enter your name: ")
print("Hello " + name + " Welcome to the number guessing game !!!")
confirmation = input("Do you wanna play (enter 'y' or 'n') ?")

def game():
    number = random.randint(1, 20)
    attempts = 0
    while confirmation == 'y':
        try:
            guess = input("Enter number between 1 & 20: ")
            if int(guess) == number:
                print("You won !!")
                attempts += 1
                print("It took you " +str(attempts)+ " to reach your goal !!! \nSo your score is "+str(attempts)+" !!")
                play_again = input("Do you wanna play again? (y/n) ")
                if play_again == 'y':
                    game()
                elif play_again == 'n':
                    print("Thanks for playing, We expect you again>>")
                    break
                    exit()
            elif int(guess) < number:
                print("Your guess is lower!!")
                attempts += 1
            elif int(guess) > number:
                print("Your guess is higher!!")
                attempts += 1
            else:
                print("Thank You!!")
        except ValueError as err:
            print("Try again!!")

game()