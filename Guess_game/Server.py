import socket
import random

HOST = "127.0.1.1"  
PORT = 5017  

def nextMove(curNum, corrNum):
    if(curNum == corrNum):
        return "EQUAL"
    if(curNum < corrNum):
        return "MORE"
    if(curNum > corrNum):
        return "LESS"

def getIntData(data):
    retValue = data.decode()
    retValue = retValue[6:]
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