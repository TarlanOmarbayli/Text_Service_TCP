# Text Service application

This application can make following operations:
- Change text: The sender sends the text file to the server and the json file, in respond the server must read the json file and swap the words from the text according the json file.
- Encode/Decodetext: The sender sends the text file and the key (another text) to the server, on the respond the server must XOR the text message with the key (One Time Pad cipher) and return it to the client. The decoding process happens in the same way where instead of the text message the client sends the encrypted text.

## Installation
Copy the following command to the console and install by pressing Enter:
```bash
https://github.com/TarlanOmarbayli/Text_Service_TCP
```
Then install all required packages:
```bash 
pip install requirements.txt
```

## Usage
- As a server, run:
```bash
python3 text_service.py server -p <port_number>
```
- As a client, run:
```bash
python3 text_service.py client --host <ip_address> -p <port_number> --mode <mode> --file1 <file_path> --file2 <file_path>
```
Note: Here file1 is a message text file and file2 can either json file or encoding/decoding key file depending on the mode option.
