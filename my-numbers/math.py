import math
from decimal import Decimal


def getAreaOfCircle(radius):
    area = math.pi * radius
    print(
        f"The value of pi is: {math.pi}, the radius is: {radius}, and the area is: {area}"
    )
    return area


print("\n===> Area of circle <===\n")
radius = 20
getAreaOfCircle(radius)

print("\n===> Infinity <===\n")
print(math.inf, float("inf"), Decimal("infinity"))

print(
    "===> All positive infinities are the same?",
    math.inf == Decimal("infinity") == float("inf"),
)

print(-math.inf, float("-inf"), Decimal("-infinity"))
print(
    "===> All negative infinities are the same?",
    -math.inf == Decimal("-infinity") == float("-inf"),
)

print("\n===> Floor & Ceil <===\n")
my_number = 6.4
c_number = math.ceil(my_number)
f_number = math.floor(my_number)
print(f"Number is equal to {my_number}")
print(f"The result of ceiling is: {c_number}, type is: {type(c_number).__name__}")
print(f"The result of floor is: {f_number}, type is: {type(f_number).__name__}")

print("\n===> absolute value, gcd, factorial <===\n")
print(f"The absolute value of -10 is : {math.fabs(-10)}")
print(f"The factorial of 5 is : {math.factorial(5)}")
print(f"The greatest common devisor of 1156 and 2264 is : {math.gcd(1156,2264)}")
