#   [0,9] == chr(48, 57)
#   [A,Z] == chr(65, 90)
#  Using Dictionary [( # == 35), ( $ == 36), ( & == 38), ( @ == 64), ( _ == 95) ]
#   [a,z] == chr(97,122)

import random as Rdm
#smbl = {35:'#', 38:'$', 64:'@', 95: '_' }
Password = list(input("Enter your password: "))

class setPassword:

    num = [chr(i) for i in range(48,58)]
    upperCase = [chr(j) for j in range(65,90)]
    lowerCase =[chr(x) for x in range(97, 122)]
    symbols = {35:'#', 38:'$', 64:'@', 95: '_' }

    def __init__(self, getpass):
        self.getpass = getpass



class passVarification(setPassword):

    def userVerification(self):
        #print(len(self.getpass))
        print("".join([str(x) for x in self.getpass]))
        #print(self.getpass)
        #print(setPassword.num)
        if len(self.getpass) < 8:
            print("Invalid Password! Password must contain 8 character including number, symbol, uppercase and lowercase letters.")
        elif len(self.getpass) <= 8:
            if any( UC in self.getpass for UC in setPassword.upperCase):
                if any( N in self.getpass for N in setPassword.num):
                    if any( LC in self.getpass for LC in setPassword.lowerCase):
                        if any( S in self.getpass for S in setPassword.symbols.values()):
                            print("Weak Password")
                        else:
                            print("Invalid Password!")
                    else:
                        print("Invalid Password!")
                else:
                    print("Invalid Password!")
            else:
                print("Invalid Password!")
        elif len(self.getpass) <= 12:
            if any( UC in self.getpass for UC in setPassword.upperCase):
                if any( N in self.getpass for N in setPassword.num):
                    if any( LC in self.getpass for LC in setPassword.lowerCase):
                        if any( S in self.getpass for S in setPassword.symbols.values()):
                            print("Medium Password")
                        else:
                            print("Invalid Password!")
                    else:
                        print("Invalid Password!")
                else:
                    print("Invalid Password!")
            else:
                print("Invalid Password!")
        elif len(self.getpass) <= 16:
            if any( UC in self.getpass for UC in setPassword.upperCase):
                if any( N in self.getpass for N in setPassword.num):
                    if any( LC in self.getpass for LC in setPassword.lowerCase):
                        if any( S in self.getpass for S in setPassword.symbols.values()):
                            print("Strong Password")
                        else:
                            print("Invalid Password!")
                    else:
                        print("Invalid Password!")
                else:
                    print("Invalid Password!")
            else:
                print("Invalid Password!")
        else:
            print("Maximum Length of Password are 16 character only! ")

newPassword = passVarification(Password)
newPassword.userVerification()
