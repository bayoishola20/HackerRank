if __name__ == '__main__':
    s = raw_input()
    answer1 = False
    answer2 = False
    answer3 = False
    answer4 = False
    answer5 = False
    for i in s:
        if i.isalnum():
            answer1 = True
        if i.isalpha():
            answer2 = True
        if i.isdigit():
            answer3 = True
        if i.islower():
            answer4 = True
        if i.isupper():
            answer5 = True
    print answer1
    print answer2
    print answer3
    print answer4
    print answer5