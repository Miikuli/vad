f = open("2ex.txt")
N = int(f.readline())
s_out = ""
upperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
specialSymbols = ["!", "@", "#", "$", "%", "&", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def checkPassword(password):
    if len(password) < 12:
        return "Invalid\n"
    hasUpperLetter = False
    hasLowerLetter = False
    hasSpecialSymbol = False
    hasNumber = False
    for symbol in password:
        if symbol in upperCaseLetters:
            hasUpperLetter = True
        elif symbol in lowerCaseLetters:
            hasLowerLetter = True
        elif symbol in specialSymbols:
            hasSpecialSymbol = True
        elif symbol in numbers:
            hasNumber = True
        else:
            return "Invalid\n"
    if (hasNumber == True and hasSpecialSymbol == True and hasLowerLetter == True and hasUpperLetter == True):
        return "Valid\n"
    else:
        return "Invalid\n"

for i in range (N):
    password = f.readline().strip()
    s_out += checkPassword(password)

print(s_out)

f.close()