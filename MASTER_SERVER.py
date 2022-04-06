import socket
import numpy as np
import encodings
import pyautogui
import sys

HOST = ''  # Standard loopback interface address (localhost)
PORT = 15001        

V = 1
VIT = 1

D = 100
DIST = 100

 
 


def switch(x, VIT, DIST):
    if( x ==  "up" ):
        pyautogui.moveRel(0, -DIST, duration = VIT) 
    elif(x ==  "down"):
        pyautogui.moveRel(0, DIST, duration = VIT) 
    elif(x ==  "left"):
        pyautogui.moveRel(-DIST, 0, duration = VIT)  
    elif(x ==  "right"):
        pyautogui.moveRel(DIST, 0, duration = VIT) 
    elif(x=="Left click"):
        pyautogui.click() 
    elif( x=="Right click"):
        pyautogui.click(button='right')
    elif( x=="Double click"):
        pyautogui.click(clicks=2)
    elif(x=="sroll up"):
        pyautogui.scroll(10)
    elif(x=="scroll down"):
        pyautogui.scroll(-10)
    elif(x == "v1"):
        VIT = V 
    elif(x =="v2"):
        VIT = V/2
    elif(x =="v3"):
        VIT = V/4
    elif(x =="v4"):
        VIT = V/8
    elif(x =="d1"):
        DIST = D
    elif(x =="d2"):
        DIST = D/2
    elif(x =="d3"):
        DIST = D/5
    elif(x =="d4"):
        DIST = D/10    
    else:
        print("no command for this input")
    
    return VIT ,DIST
        




def my_server(VIT, DIST):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server Started waiting for client to connect ")
    s.bind((HOST, PORT))

    while True:
       s.listen(5)
       client, address = s.accept()
       print("{} connected".format( address ))
       
       # Get the Data from Server and process the Data
       response = client.recv(255).decode('utf-8')
       

       if response != "":
           print("reponse : {}XX  ",response, len(response))
           print(response)
           VIT, DIST =  switch(response, VIT, DIST )
            




if __name__ == '__main__':
    my_server(VIT, DIST)
