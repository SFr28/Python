class calculator:
    """
        Class to do calculations of vector with a scalar
    """
    def __init__(self, numbers: list):
        """Initialization"""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """Addition"""
        self.numbers = [nb + object for nb in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.numbers = [nb * object for nb in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """Substraction"""
        self.numbers = [nb - object for nb in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """Division"""
        if object != 0:
            self.numbers = [nb / object for nb in self.numbers]
        else:
            print("Division by 0 is not allowed")
        print(self.numbers)
