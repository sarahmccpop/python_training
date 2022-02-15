# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

# first compare the dictionaries - compare if everything in recipe appears in available
# if yes proceed
# divide available by recipe values
# return lowest value
# if no return 0
# this doesn't pass
def cakes(recipe, available):
    checks = dict()
    # first if recipe has more ingredients than available then we can't make recipe
    if len(recipe) > len(available):
        return 0
    else:
        for key in recipe:
            for key2 in available:
                checks[key] = int(available[key] / recipe[key2])

    value_min = min(checks.values())

    return value_min


def cakes2(recipe, available):
    count = 0
    my_list = [0] * len(
        recipe
    )  ## creates a list with same number of indexes as recipes does, all 0
    ## forgot that
    for recipe_key in recipe:
        for available_key in available:
            if recipe_key == available_key:
                my_list[count] = available[recipe_key] / recipe[available_key]
                count += 1
    return int(min(my_list))


def cakes3(recipe, available):
    count = 0
    my_list = [0] * len(recipe)

    for recipe_key in recipe:
        for available_key in available:
            if recipe_key == available_key:
                my_list[count] = (
                    available[recipe_key] // recipe[available_key]
                )  ## this is the floor division operator - rounds the result down to the nearest whole number
                count += 1
    return min(my_list)


# # # must return 2
print(
    "First recipe",
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    ),
)
# # # must return 0
# print(
#     "Second recipe",
#     cakes(
#         {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
#         {"sugar": 500, "flour": 2000, "milk": 2000},
#     ),
# )
# # ALGORITHMS

# print(
#     "recipe 3",
#     cakes(
#         {"cocoa": 7, "flour": 62, "chocolate": 92},
#         {
#             "nuts": 9031,
#             "flour": 4563,
#             "pears": 59,
#             "eggs": 3068,
#             "oil": 7252,
#             "milk": 4460,
#             "cocoa": 7780,
#             "cream": 6515,
#             "butter": 1197,
#             "crumbles": 6422,
#         },
#     ),
# )

# powered by

# Solution
# def cakes(recipe, available):
#     return 5
# 1
# def cakes(recipe, available):
# 2
#     return 5
# Sample Tests
# 1


# print(
#     "Cakes 2:",
#     cakes2(
#         {"flour": 500, "sugar": 200, "eggs": 1},
#         {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
#     ),
# )

# print(
#     "Cakes 3:",
#     cakes2(
#         {"flour": 500, "sugar": 200, "eggs": 1},
#         {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
#     ),
# )
