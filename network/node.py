from typing import Optional

from config.constants import NODE_PORT
from network.network_protocol import NetworkProtocol

# Implement the Pi Network node, responsible for communication and data exchange

class Node:
    def __init__(self, node_id: int, host: str, port: Optional[int] = None):
        """
        Initialize a new node.

        :param node_id: The unique identifier of the node.
        :param host: The hostname or IP address of the node.
       :param port: The port number used by the node. If not provided, the default port number will be used.
        """
        self.node_id = node_id
        self.host = host
        self.port = port or NODE_PORT

        # Create a new network protocol instance
        self.protocol = NetworkProtocol(self)

    def start(self):
        """
        Start the node.
        """
        # Implement the node startup logic here
        # ...

        # Start the network protocol
        self.protocol.start()

    def stop(self):
        """
        Stop the node.
        """
        # Implement the node shutdown logic here
        # ...

        # Stop the network protocol
        self.protocol.stop()
