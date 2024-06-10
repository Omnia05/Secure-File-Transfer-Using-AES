#The client is the sender  
#The server is the reciever

import os
import socket

from Crypto.Cipher import AES

key = b"ThisIsMyKey:3690"                               #creating a 16 byte key and nonce (same for the server)
nonce = b"ThisIsMyNonce:19"

def encrypt_file(input_file):                           #encryptes the input file 
    try:
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        global file_size
        file_size = os.path.getsize(input_file)

        with open(input_file, "rb") as f:
            data= f.read()

        global encrypted
        encrypted = cipher.encrypt(data)

    except Exception as e:                              #if any error occurs during encryption
        print(f"Encryption error: {e}")


def send_file(file_name, new_file_name, host, port):    #sends the file to the server
    try:
        encrypt_file(file_name)                         #encryptes the file

    except Exception as e:
        print(f"Encryption error: {e}")
        return      
    
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port)) 

        client.send(new_file_name.encode('utf-8'))                     #encodes the filename, filesize and sends them
        client.send(str(file_size).encode('utf-8'))
        client.sendall(encrypted)                                      #sends the encrypted file data
        client.send(b"<END>")  

        print("File sent successfully.")
    except socket.error as e:                             #error message on encountering a socket error
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()                                    #closes the client connection 


if __name__ == "__main__":                                              #main i.e. driver's code
    send_file("Myfile.txt","Newfile.txt", '127.0.0.1', 65432)         #currently set for localhost    
    
    #send_file(file_sent, file_recieved, server's ip address, port number)
    
