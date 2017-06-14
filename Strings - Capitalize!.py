def capitalize(string):
    ans = []
    word = string.split(' ')
    for i in word:
        if i:
            ans.append(i[0].upper() + i[1:].lower())
        else:
            ans.append('')
    return ' '.join(ans)


#==================== GIVEN CODE ======================#
if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string
#===================== END =========================#