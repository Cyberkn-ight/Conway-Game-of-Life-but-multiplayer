# Conway-Game-of-Life-but-multiplayer
A Conway's Game of Life implementation that run in your terminal and allow for WAN multiplayer

To run the revised Game of Life program, first start the server by opening a terminal and navigating to the directory where the server script is saved. Then, run the following command:

```python filename.py ip port n num_cells x1,y1 x2,y2 ...```

Replace "filename.py" with the actual name of the server script file, "ip" with the IP address that the server will bind to, "port" with the port number that the server will listen on, "n" with the size of the grid, "num_cells" with the number of initial live cells, and "x1,y1 x2,y2 ..." with the starting positions of the cells (each pair of coordinates should be separated by a space).

Then, open another terminal and navigate to the directory where the client script is saved. Run the following command:

```python filename.py ip port```

Replace "filename.py" with the actual name of the client script file, "ip" with the IP address of the server, and "port" with the port number of the server.

This will start the client and connect it to the server. The client will then prompt the user to enter a move (in the form "x,y") or pause the game by entering 'p'.
