#NAME: VENKATA VIVEK  VARMA ALLURU
#DATE:05/19/1995

#This Python code defines two classes Shape and Triangle.
#The Shape class holds information about the color and filled status of a shape and
#Triangle class, a subclass of Shape, represents a triangle and calculates its area, perimeter using aformula.
#The main function prompts the user to input the lengths of the triangles sides and color.
#It check the input to form a valid triangle and displays the triangle details.


#define a class named Shape
class Shape:
    #constructor to initialize the color and filled attributes
    def __init__(self, color="black", filled=False):
        self.color = color 
        self.filled = filled  

    #returns a string representation of the object
    def __str__(self):
        #returns a string with color and filled
        return f"Color: {self.color} and Filled: {'true' if self.filled else 'false'}"

    #set the color
    def set_color(self, color):
        self.color = color

    #set the filled status
    def set_filled(self, filled):
        self.filled = filled

    #get the color attribute
    def get_color(self):
        return self.color

    def is_filled(self):
        return self.filled

#define a subclass named Triangle
class Triangle(Shape):
    #constructor to initialize the sides, color, and filled attributes
    def __init__(self, side1, side2, side3, color="black", filled=False):
        super().__init__(color, filled)  
        self.side1 = side1  
        self.side2 = side2  
        self.side3 = side3  

    #returns a string representation of the object
    def __str__(self):
        #return a string with the sides, color, and filled status
        return f"A triangle has 3 sides ({self.side1:.2f}, {self.side2:.2f}, {self.side3:.2f}), {super().__str__()}"

    #calculating the area of the triangle
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    #calculate the perimeter of the triangle
    def perimeter(self):
        return self.side1 + self.side2 + self.side3  # Return the sum of the sides

    #set the side attributes
    def set_side1(self, side1):
        self.side1 = side1

    def set_side2(self, side2):
        self.side2 = side2

    def set_side3(self, side3):
        self.side3 = side3

     #get the side attributes
    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

#function to execute the program
def main():
    while True:
        try:
            #prompt the user to enter the lengths of the sides of the triangle
            side1 = float(input("Enter side1: "))
            side2 = float(input("Enter side2: "))
            side3 = float(input("Enter side3: "))

            #checking the input sides can form a triangle
            if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
                color = input("Enter color: ")
                filled = int(input("Enter 1/0 for filled (1: true, 0: false): ")) == 1
                triangle = Triangle(side1, side2, side3, color, filled)
                #print area, perimeter, color, and filled status
                print("\n" + str(triangle))
                print(f"Has area of {triangle.area():.2f} and perimeter of {triangle.perimeter():.2f}, its color is {color} and filled is {'true' if filled else 'false'}")
                break 

            else:
                print("The input cannot form a triangle.")

        except ValueError:
            print("Input integer or floating point numbers for sides.")

if __name__ == "__main__":
    main()
