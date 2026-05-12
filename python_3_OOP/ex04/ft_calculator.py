class calculator:
    """
    Calculator class to calculate dot product, addition and substraction of vectors
    """

    @classmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculating dot product : a · b = ax × bx + ay × by"""
        dot = 0
        for i in V1:
            dot += V1[i] * V2[i]
        print("Dot product is: " + dot)

    @classmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculating addition"""
        add = [V1[i] + V2[i] for i in V1]
        print("Dot product is: " + add)

    @classmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculating subtraction"""
        add = [V1[i] - V2[i] for i in V1]
        print("Dot product is: " + sub)
