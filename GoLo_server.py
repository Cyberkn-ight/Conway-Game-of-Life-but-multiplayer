import socket
import sys

# Parse the arguments
ip = sys.argv[1]
port = int(sys.argv[2])
n = int(sys.argv[3])
num_cells = int(sys.argv[4])
positions = [(int(x), int(y)) for x, y in (coord.split(',') for coord in sys.argv[5:])]

# Initialize the grid with the given number of cells
grid = [[0 for _ in range(n)] for _ in range(n)]
for x, y in positions:
    grid[x][y] = 1

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen()

# Accept a connection from the client
client_socket, _ = server_socket.accept()

# Send the initial grid to the client
client_socket.send(bytes(f"{n}\n" + '\n'.join([' '.join(map(str, row)) for row in grid]) + "\n", "utf-8"))

# Iterate through the grid and apply the rules of the Game of Life
while True:
    # Receive a move from the client
    move = client_socket.recv(1024).decode()
    if not move:
        break

    # Update the grid
    x, y = map(int, move.split(','))
    grid[x][y] = 1

    # Count the number of live neighbors for each cell
    neighbors = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i > 0:
                neighbors[i][j] += grid[i-1][j]
            if i < n-1:
                neighbors[i][j] += grid[i+1][j]
            if j > 0:
                neighbors[i][j] += grid[i][j-1]
            if j < n-1:
                neighbors[i][j] += grid[i][j+1]
            if i > 0 and j > 0:
                neighbors[i][j] += grid[i-1][j-1]
            if i < n-1 and j < n-1:
                neighbors[i][j] += grid[i+1][j+1]
            if i > 0 and j < n-1:
                neighbors[i][j] += grid[i-1][j+1]
            if i < n-1 and j > 0:
                neighbors[i][j] += grid[i+1][j-1]

    # Update the grid based on the number of live neighbors
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and neighbors[i][j] == 3:
                grid[i][j] = 1
            elif grid[i][j] == 1 and (neighbors[i][j] < 2 or neighbors[i][j] > 3):
                grid[i][j] = 0

# Send the updated grid to the client
    client_socket.send(bytes('\n'.join([' '.join(map(str, row)) for row in grid]) + "\n", "utf-8"))

# Close the sockets
client_socket.close()
server_socket.close()
