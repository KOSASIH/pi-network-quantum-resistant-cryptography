from typing import Optional

import socket

from config.constants import NODE_BUFFER_SIZE, NODE_MAX_CONNECTIONS
from network.node import Node

# Define the network protocol used for communication between nodes

class NetworkProtocol:
    def __init__(self, node: Node):
        """
        Initialize a new network protocol instance.

        :param node: The node that this protocol belongs to.
        """
        self.node = node
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((node.host, node.port))
        self.socket.listen(NODE_MAX_CONNECTIONS)
        self.connections = []

    def start(self):
        """
        Start the network protocol.
        """
        # Implement the network protocol startup logic here
        # ...

        # Accept incoming connections
        while True:
            connection, address = self.socket.accept()
            connection.settimeout(None)
            self.connections.append((connection, address))

    def stop(self):
        """
        Stop the network protocol.
        """
        # Implement the network protocol shutdown logic here
        # ...

        # Close all connections
        for connection, _ in self.connections:
            connection.close()

        # Close the socket
        self.socket.close()
