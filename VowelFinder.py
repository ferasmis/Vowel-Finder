## Author: Feras
## Objective: A vowel finder from a string

def findVowels(s):
    vowelsFoundlist = []
    for letter in s.lower():
        if letter in ('a','e','i','o','u'):
           vowelsFoundlist.append(letter)
    print(vowelsFoundlist)
findVowels("EOhdA")