# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence:str) -> str:
    sentence_split = sentence.split(' ')
    return sentence_split[0]

def second_word(sentence:str) -> str:
    sentence_split = sentence.split(' ')
    return sentence_split[1]

def last_word(sentence:str) -> str:
    sentence_split = sentence.split(' ')
    return sentence_split[-1]



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))