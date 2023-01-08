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

print("\n>>> List Contains Item <<<\n")
print(f"my_list contains 'car'?: {'car' in my_list}")
print(f"my_list contains 'milk'?: {'milk' in my_list}")

print("\n>>> Traversing a List <<<\n")
print("traversing my_list ... Items are", end=" ")
for item in my_list:
    print(item, end=", ")

print("\ntraversing my_list2 ... Items are", end=" ")
for i in range(len(my_list2)):
    print(my_list2[i], end=", ")

for x in []:
    print("This never happens.")

print("\n>>> List Methods <<<\n")
list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.append(4)  # append only adds one value at the end of the list
print(f"list_1 after list_1.append(4) = {list_1}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.clear()
print(f"list_1 after list_1.clear() = {list_1}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
print(f"list_1.copy() = {list_1.copy()}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
print(f"list_1.copy() = {list_1.copy()}")

list_1 = [1, 2, 3, [4, 5]]
list_1_copy = list_1.copy()
print(f"list_1_copy = {list_1_copy}")
list_1[1] = 6  # changing a direct item doesn't affect the copy
print(f"list_1_copy = {list_1_copy}")

list_1[3][0] = 6  # changing a child's item affects the copy
print(f"list_1_copy = {list_1_copy}")

list_1 = [1, 2, 3, 2, 4, 2]
print(f"list_1 = {list_1}")
print(f"list_1.count(2) = {list_1.count(2)}")
# NB: list.count(val) counts the number of occurrences of the value, don't mistake with len(iterable)

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.extend([4, 5, 6, 7])
print(f"list_1.extend([4,5,6,7]) will change list_1 to {list_1}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
print(f"list_1.index(2) = {list_1.index(2)}")
