# Write your solution here
def anagrams(word1:str, word2:str) -> bool:
    return sorted(word1) == sorted(word2)


if __name__ == '__main__':
    word1 = 'python'
    word2 = 'java'
    print(anagrams(word1,word2))