# Write your solution here
def no_vowels(word:str) -> str:
    return word.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))