# Spades (♠)
import random
import time


AS = 0    # Ace of Spades
KS = 0    # King of Spades
QS = 0    # Queen of Spades
JS = 0    # Jack of Spades
S10 = 0
S9 = 0
S8 = 0
S7 = 0
S6 = 0
S5 = 0
S4 = 0
S3 = 0
S2 = 0

# Hearts (♥)
AH = 0
KH = 0
QH = 0
JH = 0
H10 = 0
H9 = 0
H8 = 0
H7 = 0
H6 = 0
H5 = 0
H4 = 0
H3 = 0
H2 = 0

# Diamonds (♦)
AD = 0
KD = 0
QD = 0
JD = 0
D10 = 0
D9 = 0
D8 = 0
D7 = 0
D6 = 0
D5 = 0
D4 = 0
D3 = 0
D2 = 0

# Clubs (♣)
AC = 0
KC = 0
QC = 0
JC = 0
C10 = 0
C9 = 0
C8 = 0
C7 = 0
C6 = 0
C5 = 0
C4 = 0
C3 = 0
C2 = 0
# Step 2: Player se card lo
print("Welcome to the Card Game!")
print("Select the card ")
x=int(input("Diamonds=1, Hearts=2, Spades=3, Clubs=4: "))
choice=0
match x:
    case 1:
        print("Diamonds")
        choice = int(input("Enter card number (1-13): "))
        choice*=3
    case 2:
        print("Hearts")
        choice = int(input("Enter card number (1-13): "))
        choice*=2
    case 3:
        print("Spades")
        choice = int(input("Enter card number (1-13): "))        
    case 4:
        print("Clubs")
        choice = int(input("Enter card number (1-13): "))    
        choice*=4
    case _:
         print("Invalid choice. Please select a valid card suit.")    


# choice = int(input("Enter card number (1-52): "))

turn = 1

# choice = int(input("Enter card number (1-52): "))

turn = 1

while True:

    num = random.randint(1, 52)

    if num == 1:

        if AS == 0:
            AS = 1
                 
            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)    
                print("User Card is Spades Ace")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                
                time.sleep(.5)
                print("Computer Card is Spades Ace")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 2:

        if KS == 0:
            KS = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades King")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades King")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 3:

        if QS == 0:
            QS = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades Queen")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades Queen")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 4:

        if JS == 0:
            JS = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades Jack")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades Jack")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 5:

        if S10 == 0:
            S10 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 10")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 10")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 6:

        if S9 == 0:
            S9 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 9")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 9")
                time.sleep(.5) 
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 7:

        if S8 == 0:
            S8 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 8")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 8")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 8:

        if S7 == 0:
            S7 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 7")
                time.sleep(.5)

                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 7")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 9:

        if S6 == 0:
            S6 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 6")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 6")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 10:

        if S5 == 0:
            S5 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 5")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 5")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 11:

        if S4 == 0:
            S4 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 4")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 4")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 12:

        if S3 == 0:
            S3 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 3")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 3")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 13:

        if S2 == 0:
            S2 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Spades 2")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Spades 2")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


#   heart 

    if num == 14:

        if AH == 0:
            AH = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts Ace")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts Ace")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 15:

        if KH == 0:
            KH = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts King")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts King")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 16:

        if QH == 0:
            QH = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts Queen")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts Queen")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 17:

        if JH == 0:
            JH = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts Jack")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts Jack")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 18:

        if H10 == 0:
            H10 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 10")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 10")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 19:

        if H9 == 0:
            H9 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 9")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 9")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 20:

        if 8 == 0:
            H8 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 8")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 8")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 21:

        if H7 == 0:
            H7 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 7")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 7")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 22:

        if H6 == 0:
            H6 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 6")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 6")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 23:

        if H5 == 0:
            H5 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 5")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 5")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 24:

        if H4 == 0:
            H4 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 4")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 4")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 25:

        if H3 == 0:
            H3 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 3")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 3")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 26:

        if H2 == 0:
            H2 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Hearts 2")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Hearts 2")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


#///////////////////////////////
    if num == 27:

        if AD == 0:
            AD = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds Ace")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds Ace")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 28:

        if KD == 0:
            KD = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds King")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds King")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 29:

        if QD == 0:
            QD = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds Queen")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds Queen")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 30:

        if JD == 0:
            JD = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds Jack")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds Jack")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 31:

        if D10 == 0:
            D10 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 10")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)           
                print("Computer Card is Diamonds 10")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 32:

        if D9 == 0:
            D9 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 9")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 9")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 33:

        if D8 == 0:
            D8 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 8")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 8")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 34:

        if D7 == 0:
            D7 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 7")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 7")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 35:

        if D6 == 0:
            D6 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)   
                print("User Card is Diamonds 6")
                time.sleep(.5) 
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 6")
                time.sleep(.5) 
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 36:

        if D5 == 0:
            D5 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 5")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 5")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 37:

        if D4 == 0:
            D4 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 4")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 4")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 38:

        if D3 == 0:
            D3 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 3")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 3")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 39:

        if D2 == 0:
            D2 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Diamonds 2")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Diamonds 2")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


#   CLUBS 

    if num == 40:

        if AC == 0:
            AC = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs Ace")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs Ace")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 41:

        if KC == 0:
            KC = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs King")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs King")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 42:

        if QC == 0:
            QC = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)   
                print("User Card is Clubs Queen")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs Queen")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 43:

        if JC == 0:
            JC = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs Jack")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")

                time.sleep(.5)
                print("Computer Card is Clubs Jack")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 44:

        if C10 == 0:
            C10 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 10")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 10")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 45:

        if C9 == 0:
            C9 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 9")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 9")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 46:

        if C8 == 0:
            C8 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 8")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 8")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 47:

        if C7 == 0:
            C7 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 7")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 7")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 48:

        if C6 == 0:
            C6 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 6")
                time.sleep(.5)

                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 6")
                time.sleep(.5)

                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 49:

        if C5 == 0:
            C5 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 5")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 5")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 50:

        if C4 == 0:
            C4 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 4")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 4")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 51:

        if C3 == 0:
            C3 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card is Clubs 3")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 3")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


    if num == 52:

        if C2 == 0:
            C2 = 1

            if turn % 2 == 1:
                print("User Side")
                time.sleep(.5)
                print("User Card 99is Clubs 2")
                time.sleep(.5)
                if num == choice:
                    print("User Wins")
                    break

            else:
                print("Computer Side")
                time.sleep(.5)
                print("Computer Card is Clubs 2")
                time.sleep(.5)
                if num == choice:
                    print("Computer Wins")
                    break

            turn += 1

        else:
            continue


                    