# loop through the alphabet and give each letter a value +1 a=# set a value to each letter in

import string
import re


alph = list(string.ascii_lowercase)

def word_score(word):
    score = 0
    word = word.lower()
    check_alph = re.findall(r'[a-z]', word)
    word_check = check_alph
    print(type(word_check))

    for i in range(len(word_check)):
        print("letter -->", len(alph))
        for j in range(0, len(alph)):
            if word_check[i] == alph[j]:
                print(j+1, alph[j])
                x = j+1
                print("---> x")
                score += x
    return score


# print(word_score("abcd545j#"))




def word_score2():
    word = input("Type a word").upper()
    wordScore=0
    for letter in word:
        letterValue=ord(letter) - 64
        wordScore += letterValue
    print(str(wordScore) + "%")

word_score2()

