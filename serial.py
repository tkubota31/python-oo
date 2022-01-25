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
    def __init__(self,start=0):
        self.change = start
        self.start = start

    def __refr__(self):
        return f"<Serial Generator start ={self.start}  next = {self.change}>"

    def generate(self):
        self.change += 1
        return self.change - 1

    def reset(self):
        self.change = self.start


    # def __init__(self, start=0):
    #     """Make a new generator, starting at start."""

    #     self.start = self.next = start

    # def __repr__(self):
    #     """Show representation."""

    #     return f"<SerialGenerator start={self.start} next={self.next}>"

    # def generate(self):
    #     """Return next serial."""

    #     self.next += 1
    #     return self.next - 1

    # def reset(self):
    #     """Reset number to original start."""

    #     self.next = self.start
