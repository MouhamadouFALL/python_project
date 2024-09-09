

# Recursion
# Une Recursion est une fonction qui s'appelle elle-meme, mais généralement avec des arguments différents.
# Dans un langage puremnent fonctionnel c'est le seul moyen de parcourir des séquence ou des boucles.
# https://www.geeksforgeeks.org/recursion-in-python/
# https://www.programiz.com/python-programming/recursion
# https://realpython.com/python-recursion/
# 

def bubble_sort(data: list[int]) -> list[int]:
    print(f"Data before sorting: {data}")
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(i, n-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
            if not swapped:
                break
    return data

def quick_sort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    pivot = data[-1]
    left = [i for i in data[:-1] if i <= pivot]
    right = [i for i in data[:-1] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# def quick_sort(data: list[int]) -> list[int]:
#     if len(data) <= 1:
#         return data
#     pivot = data[0]
#     less = [i for i in data[1:] if i <= pivot]
#     greater = [i for i in data[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

def do_operations(data: list[int]) -> None:
    # multiply each element by 2 and add 10
    for i in range(len(data)):
        data[i] = data[i] * 2 + 10

    res = bubble_sort(data)
    print(f"Result after sorting: {res}")