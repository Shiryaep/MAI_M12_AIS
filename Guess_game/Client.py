import socket

HOST = "127.0.1.1"  # The server's hostname or IP address
PORT = 5017  # The port used by the server

def printRules():
    print("This is simple guess game for numbers from 0 to 100")
    print("You will present number and server will answer")
    print("[more] if your number less then correct")
    print("[less] if your number more then correct")
    print("Lets get started!")
    print()


def getAnswer():
    isOk = False
    while(not(isOk)):
        print("Try your number", end=' :')
        inputNum = int(input())
        if (inputNum > 100) or (inputNum < 0):
            print("READ RULES!!!!!!!!!!!!!!!!!!!")
            printRules()
            isOk = False
        else:
            isOk = True
    return inputNum

def decodeData(data):
    return data.decode()

if (__name__ == "__main__"):
    printRules()
    num = getAnswer()
    count = 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(str(num).encode())
        data = s.recv(1024)
        while (decodeData(data) != "equal"):
            print("Server says: " + decodeData(data))
            num = getAnswer()
            s.sendall(str(num).encode())
            data = s.recv(1024)
            count+=1
    print(f"Great shot! Used " + str(count) + " attempt(s)")