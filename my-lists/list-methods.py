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

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.insert(2, 44)
print(f"list_1.insert(2, 44) will change list_1 to {list_1}")
# list.insert adds an item after the provided index

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
print(f"list_1.pop() = {list_1.pop()}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.remove(2)
print(f"list_1.remove(2) will change list_1 to {list_1}")

list_1 = [1, 2, 3]
print(f"list_1 = {list_1}")
list_1.reverse()
print(f"list_1.reverse() will change list_1 to {list_1}")

list_1 = [1, 2, 5, 7, 3, 6, 4]
print(f"list_1 = {list_1}")
list_1.sort()
print(f"list_1.sort() will change list_1 to {list_1}")

list_1 = ["aa", "a", "apple", "dog", "b"]
print(f"list_1 = {list_1}")
list_1.sort()
print(f"list_1.sort() will change list_1 to {list_1}")

# more on sorting, see ./inbuilt-sorting.py
