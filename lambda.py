from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers using a lambda function
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Map each number to its square using a lambda function
squared_numbers = map(lambda x: x ** 2, even_numbers)

# Reduce the squared numbers to their sum using a lambda function
sum_of_squared_numbers = reduce(lambda x, y: x + y, squared_numbers)

print("Even numbers:", list(even_numbers))
print("Squared numbers:", list(squared_numbers))
print("Sum of squared numbers:", sum_of_squared_numbers)
