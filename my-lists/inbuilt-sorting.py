import json

print("\n>>> List Sorting <<<\n")
print("==> inplace sorting (modifying the original list)")

print("### Ascending ###\n")
list_1 = [1, 2, 5, 7, 3, 6, 4]
print(f"list_1 = {list_1}")
list_1.sort()
print(f"list_1.sort() will change list_1 to {list_1}")

print("### Descending ###\n")
list_1 = [1, 2, 5, 7, 3, 6, 4]
print(f"list_1 = {list_1}")
list_1.sort(reverse=True)
print(f"list_1.sort() will change list_1 to {list_1}")

print("### using key param ###\n")
print("==> sort by length of string ###")
list_1 = ["JavaScript", "Java", "Python", "C", "C++", "Go", "AngularJS"]
print(f"list_1 = {list_1}")
list_1.sort(key=len)
print(f"list_1.sort(key=len) will change list_1 to {list_1}")

list_1 = [{"id": 4 - i, "year": 2000 + i} for i in range(4)]
print(f"list_1 = {json.dumps(list_1,indent=2)}")
list_1.sort(key=lambda element: element["id"])
print(
    f"list_1.sort(key=lambda element:element['id']) will change list_1 to {json.dumps(list_1,indent=2)}"
)
list_1.sort(key=lambda element: element["year"])
print(
    f"list_1.sort(key=lambda element:element['year']) will change list_1 to {json.dumps(list_1,indent=2)}"
)
