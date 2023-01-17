"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates new serial generator starting at start"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Representation of serial values"""
        return f"<Serial generator start={self.start} next={self.next}>"

    def generate(self):
        """Generates next number in serial sequence"""
        self.next += 1
        return self.next-1

    def reset(self):
        """Resets serial value to start value"""
        self.next = self.start

    
