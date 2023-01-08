list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print("\n>>> List operations <<<\n")
print(f"list_1 = {list_1}, list_2 = {list_2}, list_1 + list_2 = {list_1 + list_2}")
print(f"list_1 = {list_1}, list_1 * 3 = {list_1 * 3}")

print("\n>>> List Slices <<<\n")
list_3 = list_1 + list_2
print(f"list_3 = {list_3}")
print(f"list_3 all items: {list_3[:]}")
print(f"list_3 first 3 items are {list_3[:3]}")
print(f"list_3[4:] = {list_3[4:]}")
print(f"list_3[1:] = {list_3[1:]}")

print("\n>>> Modifying Items With Slices <<<\n")
list_3[3:4] = ["a", "b"]
print("Applying list_3[3:4] = ['a','b'],", end="")
print(f"list_3 = {list_3}")
list_3 = list_1 + list_2  # reset list_3

# what is happening here
# we are replacing items at the given slice range with the new values
# items outside the range are not touched
# providing less than items than the range will shorten the list
# and more values will enlarge the list
print("Applying list_3[3:] = ['a'],", end="")
list_3[3:] = ["a"]
print(f"list_3 = {list_3}")
