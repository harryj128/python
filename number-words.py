from turtle import position


terms_for_numbers = {
    '0': '',
    '00': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '01': 'one',
    '02': 'two',
    '03': 'three',
    '04': 'four',
    '05': 'five',
    '06': 'six',
    '07': 'seven',
    '08': 'eight',
    '09': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

scale_numbers = {
    '0': '',
    '1': 'thousand',
    '2': 'million',
    '3': 'billion',
    '4': 'trillion',
    '5': 'quadrillion',
    '6': 'quintillion'
}

def double(dd):
    if int(dd) < 20:
        return terms_for_numbers[dd]

    tens = terms_for_numbers[ dd[0]+'0']
    ones = terms_for_numbers[ dd[1]]
    return(f"{tens} {ones}")

def hundreds(hu):
    if hu != '0':
        return(f"{terms_for_numbers[hu]} hundred")

    return ''

number = input('Please input a number: ')
words =[]

if  len(number) % 3 != 0:
    if (len(number) + 1) % 3 == 0:
        number =  '0' + number
    elif (len(number) + 2) % 3 == 0:
        number = '00' + number

last_position = len(number)
scale_increment = 0


for x in range(len(number)-3,-1 ,-3):
    slice = number[x:last_position]
    words.insert(0,f"{hundreds(slice[0])} {double(slice[1:])} {scale_numbers[str(scale_increment)]}")
    scale_increment += 1
    last_position = x


string_list = ' '
for x in words:
    string_list += ' ' +x


print(string_list)


