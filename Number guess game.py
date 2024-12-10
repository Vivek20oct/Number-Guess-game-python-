# Number guess game python

from random import randint
def Number_guess_game():
    while True:
        try:
            print("Welcome to the Number Guessing Game!")
            print()
            print("Choose your difficulty level:")
            print('1. Beginner Level (1 to 10)')
            print('2. Intermediate Level (1 to 50)')
            print('3. Advanced Level (1 to 100)')
            print()
            game_level=int(input('Enter 1,2 or 3: '))

            if game_level==1:
                print('You played as a beginner level')
                max_num=10
                attempts=5
                

            elif game_level==2:
                print('You played as a Intermediate level')
                max_num=50
                attempts=7
                

            elif game_level==3:
                print('You played as a Advanced level')
                max_num=100
                attempts=10
                

            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print('Please enter a valid number')

        random_choice=randint(1,max_num)
        print(f"\nI have chosen a number between 1 and {max_num}. Can you guess it?")
        print(f"You have {attempts} attempts. Good luck!")
        
        for attempt in range(1, attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}/{attempts}: Your guess? "))
                if guess < 1 or guess > max_num:
                    print(f"Please guess a number between 1 and {max_num}.")
                    continue
            
                if guess == random_choice:
                    print("Congratulations! You guessed the number!")
                    print()
                    break
                elif guess < random_choice:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print(f"Sorry, you've used all your attempts. The correct number was {random_choice}. Better luck next time!")
        
        if int(input('Do you play again.Enter 1: '))==1:
            continue
        else:
            print('Thanks for Playing')
            break

Number_guess_game()
