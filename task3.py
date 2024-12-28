def isSymetrical(str):
    s = []
    pair = {"}": "{", "]": "[", ")": "("}
    for i in str:
        if(i == "{" or i == "[" or i == "("):
            s.append(i)
        elif (i == "}" or i == "]" or i == ")"):
            if(pair[i] != s.pop()):
                return False
    if(len(s)):
        return False
    return True


string = input("Enter your world: ")
if(isSymetrical(string)):
    print("It is symetrical")
else:
    print("It is not symetrical")