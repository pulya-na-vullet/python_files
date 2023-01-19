import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("192.168.31.234", 1234)
)
while True:
    data = client.recv(2048)
    print(data.decode("utf-8"))