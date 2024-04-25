class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def get_s(self):
        return self.width * self.height
    
    def get_p(self):
        return 2 * self.width + 2 * self.height
    
    def get_define_s_and_p(self):
        return self.get_s() / self.get_p()