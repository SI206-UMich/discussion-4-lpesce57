class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)

    
    def verify_input(self):
        if self.width > 0 and self.height > 0:
            return True
        else:
            return False
        
    def area(self):
        area = 0

        if self.width <= 0 or self.height <= 0:
            return "Invalid input"
        
        else:
            area = self.width * self.height

        return area

    def perimeter(self):
       perimeter = 0
       
       if self.width <= 0 or self.height <= 0:
            return "Invalid input"
            
       else:
           perimeter = (self.height * 2) + (self.width * 2)

       return perimeter
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()