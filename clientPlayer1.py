# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:50:11 2024

@author: Davud Azizov, Anthony Crivello, Ibukunoluwa
"""

import socket

# Getting the local machine's hostname. This can be used instead of 'localhost'
HOST = socket.gethostname()

# Specifying the port number
PORT = 1234

# Creating a new socket object using IPv4 addressing (AF_INET) and TCP (STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                       ipV4                TCP

# Connecting the socket to the specified host and port
client.connect((HOST, PORT))

try:
    with client:
        while True:
            
            # Receive data from the server and decode it
            response = client.recv(1024).decode()
            
            # print the data
            print(response)
            
            # check if the data contains the string "Please choose a Topic:"
            if "Please choose a Topic:" in response:
                
                # Prompt user to choose a topic
                topic = input("Enter the number next to the topic you choose: ")
                
                # Send the selected topic to the server
                client.send(topic.encode())
                
            # check if the data contains the string "Please choose a level of difficulty:"    
            elif "Please choose a level of difficulty:" in response:
                
                # Prompt user to choose a difficulty level
                level = input("Enter the number next to the difficulty level you choose: ")
                
                # Send the selected difficulty level to the server
                client.send(level.encode())
                
            # check if the data contains the string "Here is the question:"            
            elif "Here is the question:" in response:
                
                # Prompt user to answer the question
                question = input("Answer: ")
                
                # Send the user's answer to the server
                client.send(question.encode())
                
            # check if the data contains the string "This question has already been answered"               
            elif "This question has already been answered" in response:
                
                # If the question has already been answered, continue to the next iteration
                # and wait for the server's next message
                continue
            
            # check if the data starts with the string "Thanks for playing"
            # This message indicates that the game is finished
            elif "Thanks for playing" in response:
                
                # If the game is over, break out of the loop
                break
# Exception used to catch situations where the connection is unexpectedly closed or lost
except ConnectionError:
    
    # Print a message that indicates that the connection was closed unexpectly
    print("You Disconnected")

# Exception used to catch situations where the client did not type when needed or the connection closed unexpectedly
except KeyboardInterrupt:
    
    # Print a message indicating the client did not type onto the console when needed
    print("KeyBoard Interruption by player")
    
finally:
    
    # Close the client socket
    client.close()