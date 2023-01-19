import socket

server = socket.socket(
    socket.AF_INET, 
    socket.SOCK_STREAM,
)

server.bind(
    ("192.168.31.234", 1234) #localhost
)

server.listen(5) #Количество доступных подключений
print("Server is listening")

while True:
    user_socket, addres = server.accept()
    print(f"User {user_socket} connected!")
    user_socket.send("You are connected".encode("utf-8"))

