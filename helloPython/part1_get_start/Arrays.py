import numpy as np
array = np.array([1, 2, 3, 4, 5])
list = [1, 2, 3, 4, 5]
first_element = list[0]
subset = list[1:4]
list[2] = 10
list.append(6)
list.remove(4)
print(f'list: {list *2}')
print(f'first element: {first_element}')
print(f'subset: {subset}')



print(f'array: {array*2}')
print(f'first element_array: {array[0]}')
print(f'subset: {array[1:4]}')