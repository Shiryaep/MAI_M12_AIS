import socket
import random

HOST = "127.0.1.1"  
PORT = 5017  

def nextMove(curNum, corrNum):
    if(curNum == corrNum):
        return "equal"
    if(curNum < corrNum):
        return "more"
    if(curNum > corrNum):
        return "less"

def getIntData(data):
    retValue = data.decode()
    return int(retValue)

def getCodeData(answer):
    return answer.encode()

if (__name__ == "__main__"):
    while (True):
        correctNumber = random.randint(0, 100)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                print(correctNumber)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    retValue = getIntData(data)
                    retValue = nextMove(retValue, correctNumber)
                    retValue = getCodeData(retValue)
                    conn.sendall(retValue)