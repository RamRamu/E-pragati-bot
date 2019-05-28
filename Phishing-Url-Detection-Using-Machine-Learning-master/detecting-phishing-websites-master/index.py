# -*- coding: utf-8 -*-

#importing libraries
import inputScript
import pickle
import numpy as np
import socket
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#load the pickle file
classifier =  pickle.load(open('final_models/rf_final.sav','rb'))

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


def get_predict(url):
    
    #checking and predicting
    checkprediction = inputScript.generate_data_set(url)
    checkprediction= np.array(checkprediction).reshape(1,-1)
    prediction = classifier.predict(checkprediction)
    
    return prediction[0]

print("server started")

#server code
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("10.7.8.165",4446))
mysocket.listen(5)
(client,(ip,port)) = mysocket.accept()

#connecting to client
myrecsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
myrecsocket.connect(("10.7.8.30",4445))

print("connected to client")


while True:
    try :
        GPIO.output(8, GPIO.LOW) # Turn off
        data1 = myrecsocket.recv(2048).decode()
        print("start")
        print(data1)
        b = int(get_predict(data1))
        
        if(b==-1):
           GPIO.output(8, GPIO.HIGH) # Turn on
           sleep(3)

        print("end")
        print(b)
        client.send(str(b).encode())
    except:
        myrecsocket.close()
        mysocket.close()
        break

    
myrecsocket.close()
mysocket.close()
