class Cube:
    def __init__(self, side):
        self.side = side
    
    def surface(self):
        return 6 * (self.side ** 2)
    
    def volume(self):
        return self.side ** 3