'''
https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/

>>> reverse_words("the sky is blue")
'blue is sky the'
'''

def reverse_words(s: str):
    frase = s.split(' ')
    return " ".join(frase[: : -1])
