from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Creating a monster"""

    def __init__(self, first_name, is_alive=True):
        """Initializing the monster"""
        Baratheon.__init__(self, first_name, is_alive)


    def set_eyes(self, color):
        """Changing eyes color"""
        self.eyes = color


    def set_hairs(self, color):
        """Changing hairs color"""
        self.hairs = color


    def get_eyes(self):
        """Getting eyes' color"""
        return self.eyes


    def get_hairs(self):
        """Getting hairs' color"""
        return self.hairs
