class shapes:
    def __init__(self):
        self.shape_type = "Generic Shape"
class pentaon(shapes):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        import math
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.side_length ** 2)

    def perimeter(self):
        return 5 * self.side_length
    
pentagon1 = pentaon(6)
print("Area of the pentagon:", pentagon1.area())
print("Perimeter of the pentagon:", pentagon1.perimeter())
pentagon2 = pentaon(10)
print("Area of the pentagon:", pentagon2.area())
print("Perimeter of the pentagon:", pentagon2.perimeter())