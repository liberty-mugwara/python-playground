# Initializing a list
my_list = ["apples", "bananas", "milk"]
my_list2 = list((1, "lberty", True, False, []))

print("\n>>> Lists Basics <<<\n")
print(f"my_list = {my_list}, type = {type(my_list).__name__}")
print(f"my_list2 = {my_list2}, type = {type(my_list2).__name__}")

print("\n>>> Lists size/length <<<\n")
print(f"size of my_list is {len(my_list)}, size of my_list2 is {len(my_list2)}")

print("\n>>> Changing List Items <<<\n")
my_list[0] = "grapes"
print(f"my_list = {my_list}")

print("\n>>> Getting List Items <<<\n")
print(f"my_list first item is = {my_list[0]}")
print(f"my_list last item is = {my_list[-1]}")
