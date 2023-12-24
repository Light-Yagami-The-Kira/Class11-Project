import random
import datetime

def guess_loop():
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
    return attempts

def score2(P1_NAME, P1_ATTEMPTS, P2_NAME, P2_ATTEMPTS):
    P1_SCORE = 10 - P1_ATTEMPTS
    P2_SCORE = 10 - P2_ATTEMPTS

    if P1_SCORE < 0:
        P1_SCORE = 0
    if P2_SCORE < 0:
        P2_SCORE = 0

    F = open("score2.txt", "r")
    c = F.read()
    if c == "" or c == "No Record":
        q = open("score2.txt", "w")
        q.write(f"['{P1_NAME}','{P1_SCORE}'],['{P2_NAME}','{P2_SCORE}']\n")
        q.close()
    else:
        q = open("score2.txt", "a")
        q.write(f"['{P1_NAME}','{P1_SCORE}'],['{P2_NAME}','{P2_SCORE}']\n")
        q.close()
    F.close()

    if P1_SCORE == P2_SCORE:
        print(f"Game Tied with score of each {P1_SCORE}")

    else:
        if P1_SCORE > P2_SCORE:
            print(f"{P1_NAME} won with a score of {P1_SCORE} and {P2_NAME} got defeated with score of {P2_SCORE}")
        else:
            print(f"{P2_NAME} won with a score of {P2_SCORE} and {P1_NAME} got defeated with score of {P1_SCORE}")

def double_player_game():
    print("Welcome to the Double Player Guess Game")
    p1_name = input("Enter Player 1's name: ")
    p2_name = input("Enter Player 2's name: ")

    print(f"{p1_name}'s Game Has Started...")

    p1_attempts = guess_loop()

    print(f"{p2_name}'s Game Has Started")

    p2_attempts = guess_loop()
    
    score2(p1_name, p1_attempts, p2_name, p2_attempts)


def single_player_game():
    print("Welcome to the Single Player Guess Game!")
    a_a = guess_loop()
    print(f"Your score is {score(a_a)}")


def score(attempts):
    sc = 10 - attempts
    if sc < 0:
        sc = 0
    
    F = open('score.txt', 'r')
    c = F.read()
    if c == "" or c == "No Record":
        f = open("score.txt", 'w')
        f.write(f'[\'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\',\'{sc}\'];')
        f.close()
        
    else:
        f = open("score.txt", "a")
        f.write(f'[\'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\',\'{sc}\'];')
        f.close()

    F.close()
    return sc


def main():
    print("Welcome to the Guess Game!")

    while True:
        print("\nSelect an option:")
        print("1. Play Game")
        print("2. Display Score Log")
        print("3. Display High Score")
        print("4. Reset Score")
        print("5. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            u = input("1. Single Player\n2. Multiplayer: ")
            if u == '1':
                single_player_game()
            elif u == '2':
                double_player_game()
            else:
                print("Wrong Input...")
                continue

        elif choice == "2":

            u = input("1. Single Player\n2. Multiplayer: ")
            if u == '1':
                f = open("score.txt", "r")
                content = f.read().split(';')[:-1]
                if content:
                    for rec in content:
                        rec = eval(rec)
                        print(f"{rec[0]} ---> {rec[1]}")
                else:
                    print("No Record")
                f.close()
                
            elif u == '2':
                f = open("score2.txt", "r")
                content = f.read().split("\n")[:-1]
                if content:
                    for abc in range(len(content)):
                        content[abc] = (eval(content[abc]))
                    
                    for rec in content:
                        print(f"{rec[0][0]}-->{rec[0][1]} and {rec[1][0]}-->{rec[1][1]}")

                else:
                    print("No Record")
                f.close()
                
            else:
                print("Wrong Input...")
                continue

        elif choice == "3":
            u = input("1. Single Player\n2. Multiplayer: ")
            if u == '1':
                f = open("score.txt", "r")
                content = f.read().split(';')[:-1]
                if content:
                    for abcd in range(len(content)):
                        content[abcd] = eval(content[abcd])
                        content[abcd][0],content[abcd][1] = content[abcd][1],content[abcd][0]   
                    print(max(content)[1], "---->", max(content)[0])
                else:
                    print("No Record")
                f.close()
                
            elif u == '2':
                f = open("score2.txt", "r")
                content = f.read().split("\n")[:-1]
                if content:
                    for abc in range(len(content)):
                        content[abc] = (eval(content[abc]))
                
                    individual_player_list = []

                    for player1, player2 in content:

                        individual_player_list.append(player1[::-1])
                        individual_player_list.append(player2[::-1])

                    print(max(individual_player_list)[1], "--->", max(individual_player_list)[0])

                else:
                    print("No Record")
                f.close()
                
            else:
                print("Wrong Input...")
                continue


        elif choice == "4":
            file = None
            U = input("1. Single Player Score 2. Multiplayer Score: ")

            if U == '1':
                file = 'score.txt'
            elif U == '2':
                file = 'score2.txt'
            else:
                print("Wrong Input")
                continue

            f = open(file, 'w')
            f.write("No Record")
            f.close()
            print("Score Reset Completed")

        elif choice == "5":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice...")
        

if __name__ == "__main__":
    main()
