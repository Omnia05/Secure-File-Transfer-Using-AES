# Secure File Transfer Using AES

These scripts enable file transfer between two devices using AES algorithms to encrypt and decrypt the file.
The file is transmitted via TCP sockets, assumming that both the client and server know the key beforehand.

## Prerequisites

Make sure to have pycryptodome and tqdm installed, if not done already.
Instructions for installation:
    Run the following commands on your terminal.
        1. pip install pycryptodome
        2. pip install tqdm

## Instructions

To run the server script: python server.py
To run the client script: python client.py

## Note

This is my first project on AES algorithms as well as on using TCP sockets. I am completely new to these topics and this is my initial attempt to get things working. I hope to make further modifications and make my scripts more effecient. Any suggestions are always welcome.