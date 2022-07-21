book_number = '978-0-306-40615'

book_number_re = book_number.replace('-', '', -1)

print (book_number_re)

completed = 0

for  x in range(len(book_number_re)):
    if x % 2 == 0:
        completed += int(book_number_re[x])
    else:
        completed += int(book_number_re[x])* 3

completed = 10 - (completed % 10)

print(f"The completed book number is:",book_number,"-",completed)
