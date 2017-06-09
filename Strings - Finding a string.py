def count_substring(string, sub_string):
    return len([i for i in xrange(len(string)) if string.find(sub_string, i) == i])

#==================== GIVEN ======================#
if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
#===================== END =========================#