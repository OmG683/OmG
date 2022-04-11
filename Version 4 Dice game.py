

#Om
#Version three

#Log in player 1

account_1=input("Player 1 Do you have an account?\n"
              "yes or no ")
if account_1 == "no":
     choice_1=input("Do you want to make an account? ")
     if choice_1=="yes":
          username_1 = input("Please enter your username : ")
          password_1 = input("Please enter your password : ")
          print ("Greetings," , username_1, "you are now logged in now with a password")
     else:
          print("Thank you for trying my game")
          print(quit)
 

elif account_1 == "yes":
     login_username_1=input("Please enter your username : ")
     login_password_1 = input("Please enter your password : ")

     while (login_username_1 != "omg" and login_password_1 != "password1"):
           print (" Sorry username and password incorrect please re-enter for validation ")
           login_username_1=input("Please enter your username : ")
           login_password_1 = input("Please enter your password : ")
     if (login_username_1 == "omg" and login_password_1 == "password1"):
          print ("Greetings," ,login_username_1 , "you are now logged in now with a password")


#Log in player 2
account_2=input("Player 2 ,Do you have an account?\n"
              "yes or no ")
if account_2 == "no":
     username_2 = input("Please enter your username : ")
     password_2 = input("Please enter your password : ")
     print ("Greetings," , username_2, "you are now logged in now with a password")

elif account_2 == "yes":
     login_username_2=input("Please enter your username : ")
     login_password_2 = input("Please enter your password : ")

     while (login_username_2 != "keval" and login_password_2 != "abcd"):
           print (" Sorry username and password incorrect please re-enter for validation ")
           login_username_2=input("Please enter your username : ")
           login_password_2 = input("Please enter your password : ")

#dice game
from random import randint
playerOneWins = 0
playerTwoWins = 0
import random

for i in range(5):
     input("Player 1 it's your turn. Type 'roll' to roll the dice or 'quit' to forfeit. ")
     dice_roll_1=random.randint(1,6)
     dice_roll_2=random.randint(1,6)
     print("you rolled a",dice_roll_1,"and",dice_roll_2,"")
     rolltotal_1 = dice_roll_1+dice_roll_2
     if dice_roll_1 == dice_roll_2:
          double1=input("ROll AGAIN YOU GOT A DOUBLE")
          dice_roll_1=random.randint(1,6)
          print("you rolled a ",dice_roll_3,"")
          rolltotal_1= dice_roll_1 + dice_roll_2 + dice_roll_3
          print("Your total is",rolltotal_1,"")
     elif rolltotal_1 %2 == 0:
          print("You rolled an even number you get 10 points ")
          rolltotal_1= rolltotal_1+10
     else:
          rolltotal_1=rolltotal_1-5
          print("You got an odd, you lost 5 points")
          input("Player 2 it's your turn. Type 'roll' to roll the dice or 'quit' to forfeit. ")
          dice_roll_3=random.randint(1,6)
          dice_roll_4=random.randint(1,6)
          rolltotal_2 = dice_roll_3+dice_roll_4
     if dice_roll_3 == dice_roll_4:
               double2=input("ROll AGAIN YOU GOT A DOUBLE")
               dice_roll_5=random.randint(1,6)
               print("you rolled a "+str(dice_roll_5))
               rolltotal_2= dice_roll_3 + dice_roll_4 + dice_roll_5
               userOneInput = input("roll again")
     elif rolltotal_2 %2 == 0:
               print("You rolled an even number you get 10 points ")
               rolltotal_2= rolltotal_1+10
     else:
               rolltotal_1=rolltotal_1-5
               print("You got an odd, you lost 5 points")
                 
               print("Player 2 rolled ",rolltotal_2)
     if  dice_roll_3> dice_roll_4:
               print("Player 1 wins this round! ")
               playerOneWins += 1
     elif dice_roll_1 == dice_roll_2:
                print("It's a draw! ")
                playerTwoWins += 1
     else:
                print("Player 2 wins this round;")
                playerTwoWins +=1
                print("You have quit.")
                break

    
#Additional points and final score

print("Final results: ", rolltotal_1, "-", rolltotal_2)
if   rolltotal_1>  rolltotal_2:
    print("Player 1 is the winner! ")
elif  rolltotal_1 ==  rolltotal_2:
    print("It's a draw EACH PLAYER HAS ONE MORE ROLL OF A DIE! ")
    print("Player 1 it's your turn. Type 'roll' to roll the dice or 'quit' to forfeit. ")
    userOneInput = input("")
    if userOneInput == "roll":
        dice_roll_11=random.randint(1,6)
        print(dice_roll_11)
    print("Player 2 it's your turn. Type 'roll' to roll the dice or 'quit' to forfeit. ")
    userTwoInput = input("")
    if userOneInput == "roll":
        dice_roll_22=random.randint(1,6)
        print(dice_roll_22)
        
else:
    print("Player 2 is the winner! ")
#text
if rolltotal_1>  rolltotal_2:
    print("player 1")

myfile = open('externalscore.txt','rt')
line=myfile.readlines()
for x in range(0, 9):
    print(line[x])
myfile.close()
