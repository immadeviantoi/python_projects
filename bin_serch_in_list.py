lst = list(map(int, input('Введите числа в список через пробел: ').split()))
n = int(input('Введите любое число: '))


def func_to_sort(lst_to_sort):
    for i in range(len(lst_to_sort) - 1):
        for j in range(len(lst_to_sort) - 1 - i):
            if lst_to_sort[j] > lst_to_sort[j + 1]:
                lst_to_sort[j], lst_to_sort[j + 1] = lst_to_sort[j + 1], lst_to_sort[j]


func_to_sort(lst)


def bin_search(array, element, start=0, end=len(lst)):
    if start > end:
        return ('Нет элемента, удовлетворяющего условию')


    mid = (start + end) // 2
    if element > array[mid] and element <= array[mid + 1]:
        return mid


    if element < array[mid]:
        return bin_search(array, element, start, mid-1)
    else:
        return bin_search(array, element, mid+1, end)


print(bin_search(lst, n))