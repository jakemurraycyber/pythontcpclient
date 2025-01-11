import socket

target_host = '127.1.1.1' # add target URL here
target_port = 10998 # add target port here

# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
client.send(b'ABCDEF')

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()