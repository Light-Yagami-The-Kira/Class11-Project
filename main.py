import random


def single_player_game():
    print("Welcome to the Single Player Guess Game!")
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        attempts += 1
        if attempts < 11:
            try:
                guess = int(input("Enter your guess (between 1 and 100): "))
            except:
                print("Please enter a integer between 1 and 100")
                continue
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif guess < secret_number:
                if secret_number - guess > 20:
                    print("Try a very high number.")

                elif secret_number - guess > 10:
                    print("Try higher number")
                else:
                    print("Just a little more, you almost got it...")
                
            else:
                if secret_number - guess < -20:
                    print("Try a very small number.")

                elif secret_number - guess < -10:
                    print("Try smaller number")
                else:
                    print("Just a little less, you almost got it...")
                
        else:
            print("You ran out of chances.")
            break
    print(f"Your score is {score(attempts)}")


def score(attempts):
    sc = 10 - attempts
    if sc < 0:
        sc = 0

    f = open('score.txt', 'a')
    f.write(f'{sc},')
    f.close()
    return sc


def main():
    print("Welcome to the Guess Game!")

    while True:
        print("\nSelect an option:")
        print("1. Single Player")
        print("2. Display Score Log")
        print("3. Display High Score")
        print("4. Reset Score")
        print("5. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            single_player_game()

        elif choice == "2":
            f = open("score.txt", "r")
            content = f.read().split(',')[:-1]
            if content:
                print("\n".join(content))
            else:
                print("No Record")
            f.close()

        elif choice == "3":
            f = open("score.txt", "r")
            print(max(f.read().split(',')))
            f.close()

        elif choice == "4":
            f = open('score.txt', 'w')
            f.write("No Record")
            f.close()
            print("Score Reset Completed")

        elif choice == "5":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        

if __name__ == "__main__":
    main()
