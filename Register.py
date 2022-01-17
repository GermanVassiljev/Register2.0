from module2 import * 
from random import *
Login=[]
Password=[]
Login=File_Reader_Login("Login.txt",Login)
Password=File_Reader_Login("Password.txt",Password)
while True:
    a=" "
    print("<=+= MENU =+=>")
    print("<:Do you have account?:>")
    Answer=Ask_Input(a)
    if Answer.lower()=="no":
        print("<:Wanna make account?:>")
        Answer=Ask_Input(a)
        if Answer.lower()=="no":
            print("Goodbye!")
            break
        elif Answer.lower()=="yes":
            print("<:Write new login please:>")
            print("<:!Login requirements!:>")
            print("<:Not more 15 symbols:>")
            print("<:   Capital letter:>  ")
            print("<:      Numbers      :>")
            New_Login=Ask_Input(a)
            if Sign_in_Login(New_Login)==True:
                Login=Line_Saving("Login.txt",New_Login)
            print("Generate password?")
            Answer=Ask_Input(a)
            if Answer.lower()=="no":
                print("<:Write new password please:>")
                print("<:!Passowrd requirements!:>")
                print("<:Not more 12 symbols:>")
                print("<:  Capital letter :>  ")
                print("<:   Lower letter  :>  ")
                print("<:      Numbers      :>")
                New_Password=Ask_Input(a)
                if Sign_in_User_Password(New_Password)==True:
                    Password=Line_Saving("Password.txt",New_Password)
                    break
            elif Answer.lower()=="yes":
               New_Generate_Password=Sign_in_Bot_Password(Password)
               Password=Line_Saving("Password.txt",New_Generate_Password)
               print(New_Generate_Password)
               break
    elif Answer.lower()=="yes":
        if Authorization(a,Login,Password)==True:
            print("Welcome!")
        else:
            print("Wrong password or login.")
