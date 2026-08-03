import random
import time


# def show_status(user_score, computer_score):
#     print("\nCurrent Status")
#     print(f"User Score: {user_score}/100 | Progress: {user_score}%")
#     print(f"Computer Score: {computer_score}/100 | Progress: {computer_score}%")


def show_status(firstPlayer, user_score, secondPlayer, computer_score):
    print("\nCurrent Status")
    print(f"{firstPlayer}'s Score: {user_score}/100 | Progress: {user_score}%")
    print(f"{secondPlayer}'s Score: {computer_score}/100 | Progress: {computer_score}%")


print("========================================Welcome to Snack Ladder Game========================================")
user_score=0
computer_score=0
print("Play With Friend press 1 : ")
print("Play With Computer press 2  : ")
n = int(input("Enter your choice : "))

match n:
    case 1:
        
                print("Playing with the One Friend")
                time.sleep(0.2)
                user1=input("Enter the Fist Player Name : ")
                user2=input("Enter the Second Player Name : ")
                player1=0
                player2=0
                while player1<100 and player2<100:
                    print(f"\n{user1}, it's your turn!")
                    input("Press Enter to roll the dice")
                    time.sleep(0.2)
                    first=random.randint(1,6)
                    print("Dice Outcome : ",first)
                    player1+=first
                    if player1 == 100:
                       print("Player1 wins!")
                       show_status(user1, player1, user2, player2)
                       break
                    elif player1 > 100:
                        player1 -= first
                        print("Your turn is skipped!")
                        show_status(user1, player1, user2, player2)
                    else:
                        if player1 in [8, 28, 58, 80]:
                             print("You got a ladder! Moving up!")
                             player1 += 10
                        elif player1 in [13, 25, 38, 65, 17, 52, 57, 88]:
                             print("You got a snake! Moving down!")
                             player1 -= 10

                     
                        show_status(user1, player1, user2, player2)
                    
                    print(f"\n{user2}, it's your turn!")
                    input("Press Enter to roll the dice")
                    time.sleep(0.2)
                    second=random.randint(1,6)
                    print("Dice Outcome : ",second)
                    player2+=second
                    if player2 == 100:
                       print("Player2 wins!")
                       show_status(user1, player1, user2, player2)
                       break
                    elif player2 > 100:
                        player2 -= second
                        print("Your turn is skipped!")
                        show_status(user1, player1, user2, player2)
                    else:
                        if player2 in [8, 28, 58, 80]:
                             print("You got a ladder! Moving up!")
                             player2 += 10
                        elif player2 in [13, 25, 38, 65, 17, 52, 57, 88]:
                             print("You got a snake! Moving down!")
                             player2 -= 10

                     
                        show_status(user1, player1, user2, player2)
                    
                    


        
    case 2:
        print("You will play with the computer!")
        time.sleep(0.2)
        user1=input("Enter the First Player Name : ")
        user = 0
        computer = 0
        show_status(user1, user, "Computer", computer)
        while user < 100 and computer < 100:
            print("\nComputer turn")
            com = random.randint(1, 6)
            print("Computer rolled:", com)
            time.sleep(0.2)
            computer += com
            if computer == 100:
                print("Computer wins!")
                show_status(user1, user, "Computer", computer)
                break
            elif computer > 100:
                computer -= com
                print("Computer's turn is skipped!")
                show_status(user1, user, "Computer", computer)
            else:
                if computer in [8, 28, 58, 80]:
                    print("Computer got a ladder! Moving up!")
                    computer += 10
                elif computer in [13, 25, 38, 65, 17, 52, 57, 88]:
                    print("Computer got a snake! Moving down!")
                    computer -= 10

                if computer > 100:
                    computer = 100
                show_status(user1, user, "Computer", computer)

            input("Press Enter to roll the dice...")

            dice = random.randint(1, 6)
            print("You rolled:", dice)
            time.sleep(0.2)
            user += dice
            if user == 100:
                print("You wins!")
                show_status(user1, user, "Computer", computer)
                break
            elif user > 100:
                user -= dice
                print("Your turn is skipped!")
                show_status(user1, user, "Computer", computer)
            else:
                if user in [8, 28, 58, 80]:
                    print("You got a ladder! Moving up!")
                    user += 10
                elif user in [13, 25, 38, 65, 17, 52, 57, 88]:
                    print("You got a snake! Moving down!")
                    user -= 10

                show_status(user1, user, "Computer", computer)

    case _:
        print("Invalid choice!")

