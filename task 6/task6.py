class Complex:

    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __str__(self):
        if self.r != 0:
            if self.i == 1:
                return str(self.r)+ " + " + "i"
            elif self.i == -1:
                return str(self.r) + " - " + "i"
            elif self.i > 0:
                return str(self.r)+ " + " + str(self.i) + "i"
            elif self.i < 0:
                return str(self.r) + " - " + str(abs(self.i)) + "i"
            elif self.i == 0:
                return str(self.r)
        else:
            if self.i == 1:
                return "i"
            elif self.i == -1:
                return "-" + "i"
            elif self.i != 0:
                return str(self.i) + "i"
            else:
                return str(self.r)



    def __add__(self, other):
        real = self.r + other.r
        imaginary = self.i + other.i
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self.r - other.r
        imaginary = self.i - other.i
        return Complex(real, imaginary)

    def __mul__(self, other):
        real = self.r*other.r - self.i*other.i
        imaginary = self.r*other.i + self.i*other.r
        return Complex(real, imaginary)

    def __abs__(self):
        return round((self.i**2 + self.r**2)**(1/2), 2)

    def __eq__(self, other):
        if self.i == other.i and self.r == other.r:
            return True
        else:
            return False
