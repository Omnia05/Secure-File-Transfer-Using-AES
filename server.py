#The client is the sender
#The server is the reciever

import tqdm
import socket

from Crypto.Cipher import AES

key = b"ThisIsMyKey:3690"                                                  #creating a 16 byte key and nonce (same for the client)
nonce = b"ThisIsMyNonce:19"

cipher = AES.new(key, AES.MODE_EAX, nonce)

def decrypt_file(name_bytes, size_bytes):                                  #decryptes the recieved file data 
    try:
        file_name = client.recv(name_bytes).decode('utf-8')  
        print(file_name)                                                   
        file_size = client.recv(size_bytes).decode('utf-8')
        print(file_size)

        file = open(file_name, "wb")

        done = False

        file_bytes = b""

        progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))       #progress bar

        while not done:
            data = client.recv(1024)
            if file_bytes[-5:] == b"<END>":
                done= True
            else:
                file_bytes += data
            progress.update(1024)


        file.write(cipher.decrypt(file_bytes[:-5]))

        file.close()

    except Exception as e:                                                 #error message on encountering a decryption error 
        print(f"Decryption error: {e}")            


def recieve_file(host,port,nb,sb):                                         #recieves file from the client 
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #making an internet socket connection
        server.bind((host, port))
        server.listen()
        print(f"Server listening on {host}: {port}")

    except socket.error as e:
        print(f"Socket error: {e}")
        return
    
    try:                                                                    #decryptes the file
        global client
        client, addr = server.accept()  
        print(f"Connection from {addr}")

        decrypt_file(nb,sb)

        print("File received and decrypted successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:                                                                #closes the client and server
        client.close()
        server.close()     


if __name__ == "__main__":                                                  #main i.e. the driver's code
    recieve_file('127.0.0.1', 65432,12,7)                                   #currently set for localhost
    
    #recieve_file(ip address, port number, file_name_letters, size_digits)
    #replace localhost with '0.0.0.0' to listen from all interfaces





