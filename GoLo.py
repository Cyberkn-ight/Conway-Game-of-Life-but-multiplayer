import socket
import sys

# Parse the arguments
ip = sys.argv[1]
port = int(sys.argv[2])

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# Iterate through the grid and apply the rules of the Game of Life
while True:
    # Receive the grid from the server
    data = client_socket.recv(1024).decode()
    if not data:
        break
    n, *rows = data.split('\n')
    n = int(n)
    grid = [[int(cell) for cell in row.split()] for row in rows if row]

    # Print the grid
for row in grid:
    print(' '.join([str(cell) for cell in row]))
print()

# Get a move from the user
move = input("Enter a move (x,y): ")

# Send the move to the server
client_socket.send(bytes(move, "utf-8"))

# Close the socket
client_socket.close()

