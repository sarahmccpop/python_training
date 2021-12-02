lst = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]
squared_list = [no * no for no in lst]
print(squared_list)
list_of_numbers = [no for no in range(15)]
print(list_of_numbers)
divisable_by_3 = [no for no in range(50) if no % 3 == 0]
print(divisable_by_3)

names = ["sarah", "adam", "catherine", "sean"]
names_dict = {name: len(name) for name in names}
print(names_dict)
