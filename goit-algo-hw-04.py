import timeit   
import random   

def measure_time(sort_func, data):
    start_time = timeit.default_timer()                              # Ініціалізуємо початковий час
    sorted_data = sort_func(data[:])   
    execution_time = timeit.default_timer() - start_time             # Вимірюємо час виконання
    return sorted_data, execution_time

def insertion_sort(lst):
    for i in range(1, len(lst)):                                     # Проходимо по всіх елементах списку починаючи з другого
        key = lst[i]                                                 # Вибираємо ключовий елемент
        j = i - 1
        while j >= 0 and key < lst[j]:                               # Переміщуємо елементи, що більше ключа, на одну позицію вперед
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key                                             # Вставляємо ключовий елемент в правильну позицію
    return lst

def merge_sort(arr):
    if len(arr) <= 1:                                                # Перевіряємо чи довжина масиву менше або рівна 1
        return arr

    mid = len(arr) // 2                                              # Ділимо масив навпіл і отримуємо ліву та праву половини
    left_half = arr[:mid]   
    right_half = arr[mid:]   

    return merge(merge_sort(left_half), merge_sort(right_half))      # Рекурсивно сортуємо кожну половину та об'єднуємо їх

def merge(left, right):
    merged = []     
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):       # З'єднуємо елементи з обох половин
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):                                    # Додаємо залишки елементів з лівої половини
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):                                  # Додаємо залишки елементів з правої половини
        merged.append(right[right_index])
        right_index += 1

    return merged


data_smallest = [random.randint(0, 1100) for _ in range(8)]          # Генеруємо випадкові дані для тестування
data_small = [random.randint(0, 1100) for _ in range(256)]
data_big = [random.randint(0, 1100) for _ in range(1024)]
data_largest = [random.randint(0, 10000) for _ in range(8192)]

test_data = [
    data_smallest,
    data_small,
    data_big,
    data_largest
]

sorting_functions = [
    insertion_sort,
    merge_sort,
    sorted                                                            # Timsort
]

transleted_names = {
    'insertion_sort': 'Сортування вставками',
    'merge_sort': 'Сортування злиттям',
    'sorted': 'Timsort'
}

header = '{:<30} | {:<14} | {:<14} | {:<14} | {:<14}'.format('Алгоритм:', 'x10', 'x100', 'x1000', 'x10000')  # Формуємо заголовок таблиці
print(header)
print('=' * len(header))

for sort_func in sorting_functions:                                   # Проходимо по кожній функції сортування
    row = '{:<30}'.format(transleted_names[sort_func.__name__])       # Ініціалізуємо рядок для результатів
    for data in test_data:
        _, execution_time = measure_time(sort_func, data)             # Отримуємо час виконання для кожного набору даних
        row += ' | {:<14.6f}'.format(execution_time)                  # Додаємо час виконання до рядка результатів
    print(row)                                                    
