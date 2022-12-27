# Conway-Game-of-Life-but-multiplayer
A Conway's Game of Life implementation that run in your terminal and allow for WAN multiplayer

To start the server, open a terminal and navigate to the directory where the server script is saved. Then, run the following command:

```python filename.py ip port n num_cells x1,y1 x2,y2 ...```

Replace "filename.py" with the actual name of the server script file, "ip" with the IP address that the server will bind to, "port" with the port number that the server will listen on, "n" with the size of the grid, "num_cells" with the number of initial live cells, and "x1,y1 x2,y2 ..." with the starting positions of the cells (each pair of coordinates should be separated by a space).

To start the client, open another terminal and navigate to the directory where the client script is saved. Then, run the following command:

```python filename.py ip port```

Replace "filename.py" with the actual name of the client script file, "ip" with the IP address of the server, and "port" with the port number of the server.
