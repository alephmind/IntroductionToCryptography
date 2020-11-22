# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:53:42 2020

This is Bob's account.

"""

import socket 
import threading
import encoding

nickname = input("Choose a nickname: ")

# Bob's private key.
d = 14968604201641146321728426745153657588476412638052464644147687457365828709338871195
n_ = 119773458457756350072129105037472247590331967450289742152776817259249159371367389411

# Alice public key.
n = 242629063495218678744983555037677431247719090680511608679693355572526258042737530167
e = 242629063495218678744983555037677431247719090680511608679693355572526257981854870847
    
# Store public key values of other users.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

def receive():
    while True: 
    
        message = client.recv(1024).decode("utf-8")
        if message == "*NICK":
            client.send(nickname.encode("utf-8"))
        else: 
            try:
                if message.find("*") == -1:
                    message = decode_message(n_, d, message)
                    print(message)
            except: 
                pass
            #print("Client disconnected!")
            #client.close()
            #break
        
def write():
    while True: 
        message = f'{nickname}: {input("")}'
        message = encode_message(n, e, message)
        client.send(message.encode("utf-8"))
        
def encode_message(n, e, message):
    
    list_of_values = list()
    list_of_messages = encoding.string_to_4list(message)
    for subtext in list_of_messages:
        m = encoding.string2int(subtext)
        c = pow(m, e, n)
        list_of_values.append(str(c))
    return ".".join(list_of_values)

def decode_message(n_, d, message):
    
    message = message.split(".")
    values = list()
    for msg in message: 
        values.append(int(msg))
    
    subStrings = list()
    for c in values:
        m = pow(c, d, n_)
        subStrings.append(encoding.int2string(m))
    return "".join(subStrings)
    
        
receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()