class calculator:
    """
    Calculator class to calculate dot product, addition and substraction of vectors
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculating dot product : a · b = ax × bx + ay × by"""
        dot = zip(V1, V2)
        print(f"Dot product is: {sum(i*j for (i, j) in dot)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculating addition"""
        add = zip(V1, V2)
        print(f"Add vector is: {[float(i + j) for (i, j) in add]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculating subtraction"""
        print(f"Sous Vector is: {[float(i - j) for (i, j) in zip(V1, V2)]}")


# The zip() function returns a zip object, which is an iterator of tuples 
# where the first item in each passed iterator is paired together, and 
# then the second item in each passed iterator are paired together etc.
# If the passed iterables have different lengths, the iterable with the 
# least items decides the length of the new iterator.
