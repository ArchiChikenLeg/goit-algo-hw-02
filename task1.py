import queue

currentRequests = queue.Queue()
reqNumberCount = 1

class Request:
    def __init__(self, steps):
        self.stepsToResolve = steps
        self.reqNumber = globals()['reqNumberCount']
        globals()['reqNumberCount'] += 1
    
    def printInfo(self):
        return f"Request #{self.reqNumber} with {self.stepsToResolve} steps to resolve it"
    
def generateRequest():
    steps = input("Enter steps needed to resolve this request: ")
    globals()['currentRequests'].put(Request(steps))

def processRequest():
    if(globals()['currentRequests'].qsize() > 0):
        print(f"{globals()['currentRequests'].get().printInfo()} has been processed")
    else:
        print("Queue is empty! There are no requests left!")

def processAllRequests():
    while(globals()['currentRequests'].qsize() != 0):
        processRequest()


print(" 1 - create request \n 2 - process last request \n 3 - process all requests \n 0 - exit")
answer = int(input("Enter your task: "))    
while answer > 0 :
    match answer:
        case 1:
            generateRequest()
            print(" 1 - create request \n 2 - process last request \n 3 - process all requests \n 0 - exit")
            answer = int(input("Enter your task: "))   
        case 2:
            processRequest()
            print(" 1 - create request \n 2 - process last request \n 3 - process all requests \n 0 - exit")
            answer = int(input("Enter your task: "))   
        case 3:
            processAllRequests()
            print(" 1 - create request \n 2 - process last request \n 3 - process all requests \n 0 - exit")
            answer = int(input("Enter your task: ")) 
        case 0:
            break  
        case _:
            print("Invalid command! Try new other one from menu:")
            print(" 1 - create request \n 2 - process last request \n 3 - process all requests \n 0 - exit")
            answer = int(input("Enter your task: ")) 


