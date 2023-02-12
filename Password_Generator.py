# ------------------------------ Password Generator ---------------------------------------------------------
#   [0,9] == chr(48, 57)
#   [A,Z] == chr(65, 90)
#  Using Dictionary [( # == 35), ( $ == 36), ( & == 38), ( @ == 64), ( _ == 95) ]
#   [a,z] == chr(97,122)
import random as Rdm
Password = []
smbl = {35:'#', 38:'$', 64:'@', 95: '_' }

pS = input("Please choose Password Strangth; Strong(S), Medium(M), Weak(W): ").upper()

#Sp = input("Please choose Password Strangth; Strong(S), Medium(M), Weak(W): ").upper()

strong_pass = 'S' # 16 character
medium_pass = 'M' # 12 character
weak_pass = 'W'   #  8 character


class labels:

    def __init__(self, password_strength ):
        self.password_strength = password_strength

# password must contain number, symbol, uppercase_letters, lowercase_letters
# one symbol
# two numbers
# two uppercase letters
# three lowercase letters

class pw_genrator(labels):

#     def __init__(self, password_strength):
#         self.password_strength = password_strength

    def pwGen(self):
        if self.password_strength == weak_pass:
            for i in range(0,2):
                # [0-9]
                Password.append(chr(Rdm.randint(48,57)))
            #print(Password)
            for j in range(0,2):
                # [A-Z]
                Password.append(chr(Rdm.randint(65, 90)))
            #print(Password)
            for k in range(0,3):
                # [a-z]
                Password.append(chr(Rdm.randint(97, 122)))
            #print(Password)
            Password.append(Rdm.choice(list(smbl.values())))
                # [#, $, @, _]
            #print(Password)

        if self.password_strength == medium_pass:
            for i in range(0, 2):
                # [0-9]
                Password.append(chr(Rdm.randint(48, 57)))
            #print(Password)
            for j in range(0, 3):
                # [A-Z]
                Password.append(chr(Rdm.randint(65, 90)))
            #print(Password)
            for k in range(0, 6):
                # [a-z]
                Password.append(chr(Rdm.randint(97, 122)))
            #print(Password)
            Password.append(Rdm.choice(list(smbl.values())))
            # [#, $, @, _]
            #print(Password)

        if self.password_strength == strong_pass:
            for i in range(0, 2):
                # [0-9]
                Password.append(chr(Rdm.randint(48, 57)))
            #print(Password)
            for j in range(0, 3):
                # [A-Z]
                Password.append(chr(Rdm.randint(65, 90)))
            #print(Password)
            for k in range(0, 10):
                # [a-z]
                Password.append(chr(Rdm.randint(97, 122)))
            #print(Password)
            Password.append(Rdm.choice(list(smbl.values())))
            # [#, $, @, _]
            #print(Password)



PWG = pw_genrator(pS)
#spg = pw_genrator(Sp)
PWG.pwGen()
#spg.pwGen()
Rdm.shuffle(Password)
#print(Password)
new_password = "".join([str(Pass) for Pass in Password])
print(new_password)
