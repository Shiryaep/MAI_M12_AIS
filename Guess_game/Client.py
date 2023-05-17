import socket

HOST = "127.0.1.1"  
PORT = 5017  

def printRules():
    print("This is simple guess game for numbers from 0 to 100")
    print("You will present number and server will answer")
    print("[more] if your number less then correct")
    print("[less] if your number more then correct")
    print("Try with command *Guess NUM* like *Guess 50*")
    print()


def getAnswer():
    isOk = False
    while(not(isOk)):
        answer = input()
        if(not(answer[6:].isdigit()) or (answer[:5] != "Guess")):
            print("Wrong command")
        else:
            inputNum = int(answer[6:])
            if (inputNum > 100) or (inputNum < 0):
                print("READ RULES!!!!!!!!!!!!!!!!!!!")
                printRules()
                isOk = False
            else:
                isOk = True
    return answer

def decodeData(data):
    return data.decode()

if (__name__ == "__main__"):
    printRules()
    command = getAnswer()
    count = 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(command.encode())
        data = s.recv(1024)
        while (decodeData(data) != "EQUAL"):
            print("Server says: " + decodeData(data))
            command = getAnswer()
            s.sendall(command.encode())
            data = s.recv(1024)
            count+=1
    print(f"Great shot! Used " + str(count) + " attempt(s)")