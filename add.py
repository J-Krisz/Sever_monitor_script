import pickle
from server import Server

servers = pickle.load(open('servers.pickle', 'rb'))

print("Adding server")

server_name = input("enter server name")
port = int(input("Enter port number as integer"))
connection = input("Enter a type ping/http/ssl")
priority = input("Enter priority high/low")

new_server = Server(server_name, port, connection, priority)
servers.apend(new_server)

pickle.dump(servers, open("servers.picle", "rb"))
