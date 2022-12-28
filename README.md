# Conway-Game-of-Life-but-multiplayer
A Conway's Game of Life implementation that run in your terminal and allow for WAN multiplayer

#Playing the Game of Life with the Revised Server and Client Scripts

To play the Game of Life with the revised server and client scripts, you will need to follow these steps:

## - Starting the Server
Run the following command in the terminal to start the server:

```python server.py [IP] [port] [grid size] [number of initial cells] [cell 1] [cell 2] ... [cell N]```

- 'IP' is the IP address of the server. You can use localhost if you are running the server and client on the same machine.
- 'port' is the port number that the server will listen on. You can choose any available port number.
- 'grid' size is the size of the grid (number of rows and columns).
- 'number' of initial cells is the number of cells that will be present in the initial grid.
- 'cell 1' to cell N are the coordinates of the initial cells, in the form x,y.

## Starting the Client

Run the following command in the terminal to start the client:

```python client.py [IP] [port]```

- 'IP' is the IP address of the server that the client will connect to.
- 'port' is the port number that the server is listening on.

## Playing the Game
- 1: The client will receive the initial grid from the server and print it to the terminal.
- 2: You can pause the game by pressing the space bar. The game will resume when you press the space bar again.
- 3: You can also place a cell by pressing the 'e' key and entering the coordinates (x,y) of the cell you want to place.
