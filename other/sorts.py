from numpy import random


ALL_METHODS = ('select', 'insert', 'merge', 'quick')
# It's time to write some code for sortings.
def _min(elements, start_position=0):
    position = 0
    minimum = elements[0]
    for index in range(1, len(elements)):
        if elements[index] < minimum:
            position = index
            minimum = elements[index]
    return start_position + position, minimum


def _sort(_list, _method='select'):
    methods = {'select': selection_sort, 'insert': insertion_sort, 'merge': merge_sort, 'quick': quick_sort}
    if _method in methods.keys():
        return methods[_method](_list)
    else:
        raise KeyError('Unsupported _method')


# Method = select
def selection_sort(_list):
    for index in range(len(_list)):
        position, value = _min(_list[index:], index)
        while position > index:
            _list[position] = _list[position - 1]
            position -= 1
        _list[index] = value
    return _list


# Method = insert
def insertion_sort(_list):
    for index in range(1, len(_list)):
        position, value = index, _list[index]
        while _list[position - 1] > value and position > 0:
            _list[position] = _list[position - 1]
            position -= 1
        _list[position] = value
    return _list


# Method = merge
def merge_sort(_list, max_depth=-1):
    if max_depth == 0:
        return selection_sort(_list)
    mean_index = len(_list) // 2
    if len(_list) == 1:
        return _list
    left, right = merge_sort(_list[:mean_index], max_depth - 1), merge_sort(_list[mean_index:], max_depth - 1)
    index_l, index_r = 0, 0
    len_l, len_r = len(left), len(right)
    merged_list = []
    while index_l < len_l and index_r < len_r:
        if left[index_l] <= right[index_r]:
            merged_list.append(left[index_l])
            index_l += 1
        else:
            merged_list.append(right[index_r])
            index_r += 1
    if index_l + 1 < len_l:
        merged_list.extend(left[index_l:])
    else:
        merged_list.extend(right[index_r:])
    return merged_list


# Method = quick
def quick_sort(_list, max_depth=-1):
    # print(_list)
    if max_depth == 0:
        return selection_sort(_list)
    if len(_list) <= 1:
        return _list
    pivot = selection_sort([_list[0], _list[-1], _list[len(_list)//2]])[1]
    left, center, right = [], [], []
    for element in _list:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            center.append(element)
    result = quick_sort(left, max_depth-1)
    result.extend(center)
    result.extend(quick_sort(right, max_depth-1))
    return result


method = 'quick'

test_list_1 = [1, 2, 3, 4, 5, 6]
test_list_2 = [0, 0, 0, 0]
test_list_3 = [7, 352, 43, 2425, 9, 1]
test_list_4 = [6, 5, 4, 2, 3, 1]
test_list_5 = list(random.randint(0, 100, 20))

print(test_list_5)
print('==========================')
# print(_sort(test_list_1, method))
# print(_sort(test_list_2, method))
# print(_sort(test_list_3, method))
# print(_sort(test_list_4, method))
for _method in ALL_METHODS:
    print(_sort(test_list_5, _method))

