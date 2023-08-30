
from timeit import timeit 

my_list = list(range(1_000))
my_set = set(range(1_000))

list_time = timeit("999_999 in my_list", number=10, globals=globals())
print(f'List: {list_time:.6f} seconds')

set_time = timeit("999_999 in my_set", number=10, globals=globals())
print(f'Set: {set_time:.6f} seconds')

speed_difference = (list_time - set_time) / list_time * 100
print(f'{speed_difference:.3f}% faster')