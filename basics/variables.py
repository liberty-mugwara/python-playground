import json
import sys


def pretty_print(data):
    # use json to pretty print the data
    # use indent=int to do the trick
    pretty_data = json.dumps(data, indent=2)

    # print data types
    print(pretty_data, "\n\n")


NUM_VARS = 6
var1 = 4500
var2 = "liberty"
var3 = [var1, var2]
var4 = {}
var5 = set()
var6 = 4500.78


# >>> Get Data Types <<< #

# use type(data).__name__ to make it json serializable
type_data = {}
for i in range(NUM_VARS):
    val = getattr(sys.modules[__name__], f"var{i+1}")
    type_data[f"var{i+1} data type"] = type(val).__name__


print("Printing data types ...")
pretty_print(type_data)


# >>> Get Memory Locations <<< #
memory_data = {}
for i in range(NUM_VARS):
    memory_data[f"var{i+1} data location"] = (
        id(getattr(sys.modules[__name__], f"var{i+1}")),
    )

print("Printing data locations ...")
pretty_print(memory_data)

print("Demonstrating object Intering ...")
str1 = "liberty"
str2 = "liberty"
str3 = "liberty"


def check_memory_data():
    memory_data = [
        {
            "variable name": "str1",
            "value": str1,
            "data location": id(str1),
        },
        {
            "variable name": "str2",
            "value": str2,
            "data location": id(str2),
        },
        {
            "variable name": "str3",
            "value": str3,
            "data location": id(str3),
        },
    ]

    print("Printing data locations ...")
    pretty_print(memory_data)
    print(
        f"memory locations for str1, str2, and str3 are the same? {id(str1) == id(str2) == id(str3)}"
    )


check_memory_data()

print("\n\nChanging the value of str1 to 'freedom'")
str1 = "freedom"
check_memory_data()
