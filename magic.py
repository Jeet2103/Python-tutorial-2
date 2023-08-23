class Number:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            raise ValueError("Can only add instances of Number")
    
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        else:
            raise ValueError("Can only subtract instances of Number")
    
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            raise ValueError("Can only multiply instances of Number")
    
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        else:
            raise ValueError("Can only compare instances of Number")
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        else:
            raise ValueError("Can only compare instances of Number")
    
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        else:
            raise ValueError("Can only compare instances of Number")
    
    def __le__(self, other):
        if isinstance(other, Number):
            return self.value <= other.value
        else:
            raise ValueError("Can only compare instances of Number")

# Create instances of Number
num1 = Number(5)
num2 = Number(3)
# Test the operations and comparisons
print("num1:", num1)
print("num2:", num2)
print("num1 + num2:", num1 + num2)
print("num1 - num2:", num1 - num2)
print("num1 * num2:", num1 * num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)
print("num1 > num2:", num1 > num2)
print("num1 <= num2:", num1 <= num2)
