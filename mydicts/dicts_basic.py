from utils.util import prettyPrint

my_dict = {"id": 1, "name": "Liberty", "age": 26}
my_dict2 = dict([("id", 1), ("name", "Liberty"), ("age", 26)])

print("\n>>> Dict Basics <<<\n")
print(f"my_dict = {prettyPrint(my_dict)}, type = {type(my_dict).__name__}")
print(f"my_dict2 = {prettyPrint(my_dict2)}, type = {type(my_dict2).__name__}")
