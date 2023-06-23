def bubble_sort(keyword, list_data):
    for i in range(len(list_data)):
        for j in range(len(list_data) - i - 1):
            if str(list_data[j]).lower() > str(list_data[j+1]).lower():
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]
    return binary_search(keyword, list_data)

def binary_search(keyword, list_data):
    left = 0
    right = len(list_data) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(list_data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(list_data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(list_data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

list_data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1 ]
keyword = input("Input keyword: ")
bubble_sort(keyword, list_data)