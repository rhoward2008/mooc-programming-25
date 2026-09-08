import string

def change_case(orig_string: str) -> str:
    change = ''
    for char in orig_string:
        if char in string.ascii_lowercase:
            change += char.upper()
        elif char in string.ascii_uppercase:
            change += char.lower()

    return change

def split_in_half(orig_string: str) -> tuple:
    half_way = int(len(orig_string)/2)
    part1 = orig_string[0:half_way]
    part2 = orig_string[half_way:]

    return part1,part2

def remove_special_characters(orig_string: str) -> str:
    removed_char = ''

    for char in orig_string:
        if char in string.ascii_letters or char in string.ascii_uppercase or char in string.digits or char in string.whitespace:
            removed_char += char

    return removed_char

if __name__ == '__main__':
    p1 = change_case('AbCdE')
    #print(p1)

    p2 = split_in_half('abcdef')
    #print(p2)

    p3 = remove_special_characters('ab5% CD')
    print(p3)