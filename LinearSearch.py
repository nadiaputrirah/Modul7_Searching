def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

data = [9, 12, 8, 4, 10, 32, 45]
keyword = input("Input keyword: ")
linear_search(keyword, data)
