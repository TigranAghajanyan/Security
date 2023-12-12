# Function to calculate the GCD using the Euclidean algorithm
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input numbers
a = 48
b = 18

# Calculate the GCD
gcd = calculate_gcd(a, b)

# Print the GCD
print("The GCD of", a, "and", b, "is", gcd)
import math

# Input numbers
a = 48
b = 18

# Calculate the LCM
lcm = abs(a * b) // math.gcd(a, b)

# Print the LCM
print("The LCM of", a, "and", b, "is", lcm)
