from random import *
def File_Reader_Login(f: str,l:list):
    """Information from file f to list l
    """
    file=open(f,"r")
    for i in file:
        l.append(i.strip())
    file.close()
    return l
def File_Reader_Password(f: str,c:list):
    """
    """
    file=open(f,"r")
    for i in file:
        c.append(i.strip())
    file.close()
    return c
def File_Saving(f:str,l:list):
    file=open(f,"w")
    for i in l:
        file.write(i+"\n")
    file.close()
def Line_Saving(f:str,line:str):
    file=open(f,"a")
    file.write(line+"\n")
    file.close()
def Ask_Input(a: str):
    """Ask user anythink
    :param str a: String of user
    :rtype: str
    """
    a=str(input("=>"))
    return a
def Sign_in_Login(a: str):
    """Registration new login 
    :param str a: New login
    :rtype: list
    """
    passOK=True
    str0 = ".,:;!_*-+()/#¤%&"
    alpha=digit=upper=speacial=0
    ls = list(str0)
    aR=list(a)
    for i in range(len(aR)):
        if aR[i].isupper():
            upper=1
        if aR[i].isalpha():
            alpha = 1
        if aR[i].isdigit():
            digit = 1
        if aR[i] in ls:
            speacial=1
    if alpha == 1 and digit==1 and upper==1 and speacial==1 and len(aR)<=15:
        passOK=True
    else:
        passOK=False
    return passOK
def Sign_in_User_Password(a: str):
    """Registration User password
    :param str a: New password
    :rtype: list
    """
    passOK=True
    str0 = ".,:;!_*-+()/#¤%&"
    alpha=digit=upper=speacial=0
    ls = list(str0)
    aR=list(a)
    for i in range(len(aR)):
        if aR[i].isupper():
            upper=1
        if aR[i].isalpha():
            alpha = 1
        if aR[i].isdigit():
            digit = 1
        if aR[i] in ls:
            speacial=1
    if alpha == 1 and digit==1 and upper==1 and speacial==1 and len(aR)<=12:
        passOK=True
    else:
        passOK=False
    return passOK
def Sign_in_Bot_Password(c: list):
    """Create new password for User
    :param list c: List of passwords
    :rtype: list
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    Generate_Password=list(str4)
    shuffle(Generate_Password)
    password = "".join([choice(Generate_Password) for x in range(12)])
    c.append(password)
    return password
def Authorization(a: str,b: list,c: list):
    """Authorization user
    :param list b: List of logins
    :param list c: List of passwords
    :param str a: User answers
    :rtype: bool
    """
    passOK=True
    while True:
        print("<:Write your login please:>")
        g=Ask_Input(a)
        print("<:Write your password please:>")
        h=Ask_Input(a)
        if  g in b and h in c and b.index(g)==c.index(h):
            passOK=True
            return passOK
        else:
            print("Oops! Somethink wrong! Try again please.")
            passOK=False
            return passOK

