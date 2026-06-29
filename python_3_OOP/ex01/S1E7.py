from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name, is_alive=True):
        """Creating a Baratheon member"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self) -> str:
        """
        Informal string representation of the object,
        aimed at the user
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Official string representation of the object,
        aimed at the programmer
        """
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name, is_alive=True):
        """Creating a Lannister member"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self) -> str:
        """
        Informal string representation of the object,
        aimed at the user
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Official string representation of the object,
        aimed at the programmer
        """
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Creating a Lannister member"""
        return cls(first_name, is_alive)
