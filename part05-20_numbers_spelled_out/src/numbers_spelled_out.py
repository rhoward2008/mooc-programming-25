# Write your solution here
def dict_of_numbers() -> dict:
    number_word_dict = {}

    num_lookup = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            15: 'fifteen',
            18: 'eighteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'

    }

    for num in range(0,100):
        if num in num_lookup:
            number_word_dict[num] = num_lookup[num]
        elif 13 < num < 20:
            number_word_dict[num] = num_lookup[num%10] + 'teen'
        else:
            number_word_dict[num] = num_lookup[(num//10)*10] + '-' + num_lookup[num%10]

    return number_word_dict


if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers)