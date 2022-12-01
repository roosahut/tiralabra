class Node:
    """The class of the node in the graph.
    """

    def __init__(self, id: int, position: tuple, neighbours: dict):
        """The constructor.

        Args:
            id (int): The id of the node.
            position (tuple): The position of the node in latitude and longitude.
            neighbours (dict): The neighbour nodes.
        """
        self.id = id
        self.position = position
        self.neighbours = neighbours
