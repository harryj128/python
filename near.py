def near(string_a, string_b):
    '''Given two strings of letters, determine whether the second can be made from the first by removing one letter.'''
    # doc string / tool tip
    if len(string_a) != (len(string_b) + 1):
        print('Strings differ by more than 1')
        return False

    for x in range(len(string_a)):
        compare_string = string_a[0:x] + string_a[x+1:]
        print( f'{compare_string},{string_b}')
        if compare_string == string_b:
            print("It's a match!")
            return True

    return False

print(near('reset', 'rest'))








def near2 (string_a, string_b):
    if len(string_a) - len(string_b) != 1:
        return False

    for letter in string_a:
        compare_string = string_a.replace(letter, '',)
        print(compare_string)
        if compare_string == string_b:
            return True


