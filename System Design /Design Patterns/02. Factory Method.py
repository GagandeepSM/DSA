class Shape:
    def draw(self):
        pass
        
class Circle(Shape):
    def draw(self):
        print('Draw Circle:')
    
class Square(Shape):
    def draw(self):
        print('Draw Square: ')

class ShapeFactory:
    def create(self, kind):
        if kind == 'circle':
            return Circle()
        if kind == 'square':
            return Square()
    
factory = ShapeFactory()
shape = factory.create('circle')
shape.draw()
