from abc import ABC, abstractmethod


class Character(ABC):
    """Creating a class Character that takes a first name and a live status"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor:
        Initializing first name and live status, is_alive is true by default"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to change live status from True to False"""
        self.is_alive = False


class Stark(Character):
    """Creating a class Stark that inherits from Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor: calling Character constructor with\
 a name and a non mandatory live status"""
        Character.__init__(self, first_name, is_alive)
