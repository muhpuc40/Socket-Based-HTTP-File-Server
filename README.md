Socket-Based HTTP File Server
This project implements a simple HTTP file server and client using Python's socket programming. The server listens for client requests, serves requested files over TCP, and returns a 404 error if the file is not found. The client sends HTTP GET requests to retrieve files from the server.
Prerequisites

Python 3.x: Ensure Python 3 is installed. Check with:
python --version

or
python3 --version

Download from python.org if needed.

Files:

server.py: The server script that handles file requests.
client.py: The client script that sends HTTP GET requests.
A test file (e.g., test.txt): A sample file to request from the server.


Network:

For local testing, use 127.0.0.1 or localhost.
For network testing, ensure the server’s IP (e.g., 192.168.0.106) is accessible and not blocked by a firewall.



Setup

Clone the Repository:
git clone https://github.com/<your-username>/Socket-Based-HTTP-File-Server.git
cd Socket-Based-HTTP-File-Server


Create a Test File:

Create a file named test.txt in the project directory with some content:echo "Hello, this is a test file!" > test.txt

or manually create test.txt with a text editor and add content, e.g.:Hello, this is a test file!




Directory Structure:
Socket-Based-HTTP-File-Server/
├── server.py
├── client.py
├── test.txt



Running the Project
Step 1: Start the Server

Open a terminal in the project directory:
cd /path/to/Socket-Based-HTTP-File-Server


Run the server:
python server.py

or
python3 server.py


The server will display:
The Server <hostname> is running ...


The server listens on IP 192.168.0.106 and port 65000 by default.
For local testing, you may need to change the IP in server.py to 127.0.0.1:serverSocket.bind(('127.0.0.1', serverPort))

Save and restart the server if changed. If 192.168.0.106 is correct for your setup, proceed as is.



Step 2: Run the Client

Open another terminal in the project directory:
cd /path/to/Socket-Based-HTTP-File-Server


Run the client to request test.txt:
python client.py 192.168.0.106 65000 test.txt

or, if using 127.0.0.1:
python client.py 127.0.0.1 65000 test.txt

or
python3 client.py 127.0.0.1 65000 test.txt


Expected Output:

Client Output:
HTTP/1.1 200 OK

Hello, this is a test file!


Server Output:
The Server <hostname> is running ...
Request from client ('<client_ip>', <client_port>) on port <thread_name> ...
Filename requested is /test.txt
Success File sent !


If the file is not found, the client will show:
HTTP/1.1 404 Not Found

and the server will show:
Requested File not available.





Step 3: Stop the Server

Press Ctrl+C in the server terminal to stop the server.

Troubleshooting

Address Already in Use:

If port 65000 is in use, change it in server.py (e.g., to 65001) or free the port:lsof -i :65000
kill -9 <pid>




Connection Refused:

Ensure the server is running and the IP/port in the client command match those in server.py.
Verify 192.168.0.106 is the server’s IP (use ifconfig, ip addr, or ipconfig to check). For local testing, use 127.0.0.1.


File Not Found (404):

Confirm test.txt exists in the project directory.
Ensure the filename in the client command matches exactly (case-sensitive).


Limited Output:

The client receives up to 1024 bytes, sufficient for small files like test.txt. Larger files may be truncated.



Notes

The server sends files character by character, which is inefficient but works for small files.
You can create additional test files and request them, e.g.:python client.py 127.0.0.1 65000 otherfile.txt


This is a basic implementation for educational purposes and lacks features like proper HTTP headers or security measures.

License
This project is licensed under the MIT License.
