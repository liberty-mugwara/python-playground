# built in types
var_int = 10000000
var_float = 4500.89
var_complex = 58 + 9j

print(f"type of var_int is: {type(var_int)}\n")
print(f"type of var_float is: {type(var_float)}\n")
print(f"type of var_complex is: {type(var_complex)}\n")

# big number separators
big_number = 1_000_000_000
print(f"type of big_number is: {type(big_number)} and value is:{big_number}\n")

# exponential values are always floats
e_notation_number = 1e6
print(
    f"type of e_notation_number is: {type(e_notation_number)} and value is:{e_notation_number}\n"
)
# converting numbers
print("======> converting numbers <======\n")
var_int = 10
var_float = 9.7

var_int_as_float = float(var_int)
print(f"Converting {var_int} to float: New value is equal to {var_int_as_float}\n")

var_float_as_int = int(var_float)
print(
    f"Converting {var_float} to interger: New value is equal to {var_float_as_int}\n NB: It rounds down.\n"
)

# arithmetic operations
var_int = 10
var_float = 4.5
print("======> arithmetic operations <======\n")
print("### Adition ###\n")
print(
    f"{type(var_int).__name__} + {type(var_int).__name__} = {type(var_int + var_int).__name__}"
)
print(
    f"{type(var_int).__name__} + {type(var_float).__name__} = {type(var_int + var_float).__name__}"
)
print(
    f"{type(var_float).__name__} + {type(var_float).__name__} = {type(var_float + var_float).__name__}"
)

print("\n### Subtraction ###\n")
print(
    f"{type(var_int).__name__} - {type(var_int).__name__} = {type(var_int - var_int).__name__}"
)
print(
    f"{type(var_int).__name__} - {type(var_float).__name__} = {type(var_int - var_float).__name__}"
)
print(
    f"{type(var_float).__name__} - {type(var_float).__name__} = {type(var_float - var_float).__name__}"
)

print("\n### Multiplication ###\n")
print(
    f"{type(var_int).__name__} * {type(var_int).__name__} = {type(var_int * var_int).__name__}"
)
print(
    f"{type(var_int).__name__} * {type(var_float).__name__} = {type(var_int * var_float).__name__}"
)
print(
    f"{type(var_float).__name__} * {type(var_float).__name__} = {type(var_float * var_float).__name__}"
)

print("\n### Division ###\n")
print(
    f"{type(var_int).__name__} / {type(var_int).__name__} = {type(var_int / var_int).__name__}"
)
print(
    f"{type(var_int).__name__} / {type(var_float).__name__} = {type(var_int / var_float).__name__}"
)
print(
    f"{type(var_float).__name__} / {type(var_float).__name__} = {type(var_float / var_float).__name__}"
)

print("\n### Floor Division ###\n")
print(
    f"{type(var_int).__name__} // {type(var_int).__name__} = {type(var_int // var_int).__name__}"
)
print(
    f"{type(var_int).__name__} // {type(var_float).__name__} = {type(var_int // var_float).__name__}"
)
print(
    f"{type(var_float).__name__} // {type(var_float).__name__} = {type(var_float // var_float).__name__}"
)

print("\n### Exponential Operator ###\n")
print(
    f"{type(var_int).__name__} ** {type(var_int).__name__} = {type(var_int ** var_int).__name__}"
)
print(
    f"{type(var_int).__name__} ** {type(var_float).__name__} = {type(var_int ** var_float).__name__}"
)
print(
    f"{type(var_float).__name__} ** {type(var_float).__name__} = {type(var_float ** var_float).__name__}"
)

print("\n### Modulas Operator ###\n")
print(
    f"{type(var_int).__name__} % {type(var_int).__name__} = {type(var_int % var_int).__name__}"
)
print(
    f"{type(var_int).__name__} % {type(var_float).__name__} = {type(var_int % var_float).__name__}"
)
print(
    f"{type(var_float).__name__} % {type(var_float).__name__} = {type(var_float % var_float).__name__}"
)

print("\n### Check if value is a number ###\n")


def isNum(variable):
    return type(variable) in [int, float, complex]


print(isNum(67))
print(isNum(45.88))
print(isNum(1 + 2j))
print(isNum("78,99"))
print(isNum(True))
print(isNum([78, 99]))
print(isNum((78, 99)))
