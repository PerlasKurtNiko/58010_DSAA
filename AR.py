class rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def display_area(self):
        print(self.area())

rectangle = rectangle(3, 4)
rectangle.display_area()
