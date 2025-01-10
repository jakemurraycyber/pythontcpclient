import socket

target_host = 'www.python.org' # add target URL here
target_port = 443 # add target port here

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
client.send(b'GET / HTTP/1.1\r\nHOST: python.org\r\n\r\n')

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()