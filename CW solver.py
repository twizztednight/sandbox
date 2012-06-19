#Brett Zimmermann
#06/06/2012

#global
import codecs
import re
data = { }
#main
def main():
    wordlist = codecs.open("words.txt", "r", "utf-8")
    sanitize(wordlist)
    menu()
    wordlist.close()
#basic sanitization
def sanitize(wordlist):
    for word in sorted(wordlist):
        
        data.setdefault(word,[]).append(word)
  
    #menu
def menu():
    
    try:
        while True:
            print('~' *30)
            print("Word Play \n1.) Anagram Solver \n2.) Crossword Solver \n3.) Palindrome Finder" \
              "\n4.) Letter Frequency \n0.) Exit")
            listnum = int(input("\nPlease Select a Menu Option: "))
            if listnum == 1:
                anagram()
            elif listnum == 2:
                crossword()
            elif listnum == 3:
                palindrome()
            elif listnum == 4:
                letterfreq(data)
            else:
                if listnum == 0:
                    break
    except ValueError:
        print("You have entered an invalid option. Please try again.")
        menu()
#anagram
def anagram():
    word = input("What are the letters? ")
    for line in data:
        line = line.strip()
        if len(line) == len(word):
            if anagramchk(line, word):
                print( line)
    
#anagram check   
def anagramchk(word, chkword):
    for ch in word:
        if ch in chkword:
            chkword = chkword.replace(ch, ' ', 1)
        else:
            return 0
    return 1

#palindrome        
def palindrome():
    word = input("What is the word you are checking? ")
    print(word)
    i = 0
    while i < len(word)/2:
        if word[i] != word[-1-i]:
            print("This word is not a Palindrome")
            return
        i = i+1
    print("This word is a Palindrome")

#crossword
def crossword():
    word = input(" Use ? as a wildcard, \n Please input letters and wildcards: ")
    for line in data:
        line = line.strip()
        if len(line) == len(word):
            good = 1
            pos = 0
            for letter in word:
                if not letter == '?':
                    if not letter == line[pos]:
                        good = 0
                pos+=1
            if good ==1:
                print(line)
                
 #letter frequency          
def letterfreq(data):
    ltrfreq = {}
    char_count = 0
    for word in data:
        for char in word.lower().strip():
            char_count += 1
            if char in ltrfreq:
                ltrfreq[char] += 1
            else:
                ltrfreq[char] = 1
    print("Following is the letter frequency of the dictionary. " ,'\n',ltrfreq, '\n')
    
main()
