from collections import deque


def isPalindrom(str):
    str = str.lower()
    mainDeque = deque()
    for i in str:
        if(i != ' '):
            mainDeque.append(i)
    while(len(mainDeque) > 1):
        if(mainDeque.popleft() != mainDeque.pop()):
            return False
    return True


world = input("Enter your world: ")

if (isPalindrom(world)):
    print("It is palindrom!")
else:
    print("It is not palindrom( Try anouther time!")