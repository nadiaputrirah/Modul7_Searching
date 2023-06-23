def linear_search(keyword, list_data):
    for i in range(len(list_data)):
        if str(list_data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

list_data = ['R 2477 SR', 'R 1234 DJ', 'R 7015 LP', 'R 0201 RR', 
        'R 3304 DA', 'R 2401 SK', 'R 2103 RT', 'R 1708 RI', 'R 1111 SR',
          'R 4987 LH']
keyword = input("Input keyword: ")
linear_search(keyword, list_data)