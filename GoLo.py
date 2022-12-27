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
    move = input("Enter a move (x,y) or 'p' to pause: ")

    # If the user wants to pause the game, disconnect from the server and enter single player mode
    if move == 'p':
        client_socket.close()
        while True:
            # Get a move from the user
            move = input("Enter a move (x,y) or 'c' to connect to a server: ")

            # If the user wants to connect to a server, reconnect to the server and continue the game
            if move == 'c':
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((ip, port))
                break

            # Parse the move
            x, y = map(int, move.split(','))

            # Update the grid
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

            # Print the grid
            for row in grid:
                print(' '.join([str(cell) for cell in row]))
            print()
    else:
        # Send the move to the server
        client_socket.send(bytes(move, "utf-8"))

# Close the socket
client_socket.close()
