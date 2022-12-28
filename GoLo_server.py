import socket
import sys
import time

# Parse the arguments
ip = sys.argv[1]
port = int(sys.argv[2])
n = int(sys.argv[3])
num_cells = int(sys.argv[4])
cells = [tuple(map(int, cell.split(','))) for cell in sys.argv[5:]]

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen()

# Set up the initial grid
grid = [[0 for _ in range(n)] for _ in range(n)]
for x, y in cells:
    grid[x][y] = 1

# Wait for a client to connect
client_socket, client_address = server_socket.accept()

# Send the initial grid to the client
client_socket.send(bytes(f"{n}\n" + '\n'.join([' '.join(map(str, row)) for row in grid]) + "\n", "utf-8"))

# Iterate through the grid and apply the rules of the Game of Life
while True:
    # Receive a move from the client
    move = client_socket.recv(1024).decode().strip()

    # Check if the client wants to pause the game
    if move == 'p':
        # Wait for the client to resume the game
        move = client_socket.recv(1024).decode().strip()

    # Check if the client wants to place a cell
    elif move == 'e':
        # Receive the coordinates of the cell to be placed
        x, y = map(int, client_socket.recv(1024).decode().strip().split(','))
        grid[x][y] = 1

    # Update the grid based on the number of live neighbors
    neighbors = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < n and 0 <= j + y < n:
                        neighbors[i][j] += grid[i + x][j + y]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and neighbors[i][j] == 3:
                grid[i][j] = 1
            elif grid[i][j] == 1 and (neighbors[i][j] < 2 or neighbors[i][j] > 3):
                grid[i][j] = 0

    # Send the updated grid to the client
    client_socket.send(bytes(f"{n}\n" + '\n'.join([' '.join(map(str, row)) for row in grid]) + "\n", "utf-8"))

# Close the socket
client_socket.close()
server_socket.close()
