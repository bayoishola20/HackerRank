if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    max_possibility = -101
    second_largest_number = -101
   
    for i in arr:
        if i > max_possibility:
            max_possibility = i
    
    for i in arr:
        if (i > second_largest_number) and (i < max_possibility):
            second_largest_number = i
    print second_largest_number