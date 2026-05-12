from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Creating a monster"""

    def set_eyes(self, color) -> None:
        """Changing eyes color"""
        self.eyes = color

    def set_hairs(self, color) -> None:
        """Changing hairs color"""
        self.hairs = color

    def get_eyes(self) -> str:
        """Getting eyes' color"""
        return self.eyes

    def get_hairs(self) -> str:
        """Getting hairs' color"""
        return self.hairs
