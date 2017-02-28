def pairing(parenthesh):
    metrhths1 = 0
    for i in parenthesh:
        if i == "(":
            metrhths1 = metrhths1 + 1
        elif i == ")":
            metrhths1 = metrhths1 - 1
        if metrhths1 < 0:
            return False
    
    return metrhths1 == 0
ParenthesisNumber = raw_input("H akolouthia einai: ")

print pairing(ParenthesisNumber)