import copy
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def read_words(file_name):
    file = open(file_name, 'r')
    words = file.readlines()
    file.close()
    copy000 = copy.deepcopy(words)
    copy111 = copy.deepcopy(words)
    copy222 = copy.deepcopy(words)

    start = time.time()
    sorted_words0 = sorted(copy000)
    end = time.time()
    print(f"Time taken by sorted(): {end - start} seconds ")

    start = time.time()
    sorted_words1 = quicksort(copy111)
    end = time.time()
    print(f"Time taken by quicksort(): {end - start} seconds ")

    start = time.time()
    sorted_words2 = insertionSort(copy222)
    end = time.time()
    print(f"Time taken by insertionSort(): {end - start} seconds ")


file_name = r'C:\Users\natas\Desktop\uni\FoP\week 13\pseudo_words.txt'
read_words(file_name)