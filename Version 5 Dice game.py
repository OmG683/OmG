#Om

#Log in player 1
#This is my player one log in system wich allows the player to input 
def login1():
    global login1
    login_username_1 = input("Please enter your username : ")
    login_password_1 = input("Please enter your password : ")



account_1=input("Player 1 Do you have an account?\n"
                "yes or no ")
if account_1 == "no":
         choice_1=input("Do you want to make an account? ")
         if choice_1=="yes":
             login1()
             print ("Greetings," , login_username_1, "you are now logged in now with a password")    
         else:
             print("Thank you for trying my game")
             print(quit)
elif account_1 == "yes":
    login1()
    if(login_username_1 != "omg" and login_password_1 != "password1"):
        print (" Sorry username and password incorrect please re-enter for validation ")
    elif (login_username_1 == "omg" and login_password_1 == "omg"):
              myfile = open('user1.txt','rt')
              contents= myfile.read()
              print(contents)
              myfile.close()
            
                  


