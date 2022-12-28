import socket
import sys
import msvcrt

# Parse the arguments
ip = sys.argv[1]
port = int(sys.argv[2])

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

# Receive the initial grid from the server
data = client_socket.recv(1024).decode().split('\n')
n = int(data[0])
grid = [[int(cell) for cell in row.split()] for row in data[1:]]

# Print the initial grid
print('\n'.join([' '.join(map(str, row)) for row in grid]))

# Iterate through the grid and apply the rules of the Game of Life
while True:
    # Check if the user wants to pause the game
    if msvcrt.kbhit() and msvcrt.getch() == b' ':
        # Send the pause instruction to the server
        client_socket.send(bytes("p\n", "utf-8"))

        # Receive the updated grid from the server
        data = client_socket.recv(1024).decode().split('\n')
        grid = [[int(cell) for cell in row.split()] for row in data[:-1]]

        # Print the updated grid
        print('\n'.join([' '.join(map(str, row)) for row in grid]))

    # Check if the user wants to place a cell
    elif msvcrt.kbhit() and msvcrt.getch() == b'e':
        # Prompt the user to enter the coordinates of the cell
        x, y = map(int, input("Enter the coordinates (x,y) of the cell: ").split(','))

        # Send the placement instruction and the coordinates to the server
        client_socket.send(bytes("e\n", "utf-8"))
        client_socket.send(bytes(f"{x},{y}\n", "utf-8"))

# Close the socket
client_socket.close()
