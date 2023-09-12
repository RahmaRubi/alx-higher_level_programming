class MyInt(int):
    """ myint class """
    def __init__(self, value):
        super().__init__()

    def __eq__(self, other):
        # Override the equality (==) operator
        return super().__ne__(other)

    def __ne__(self, other):
        # Override the inequality (!=) operator
        return super().__eq__(other)
