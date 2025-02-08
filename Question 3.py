#Question 3
wordlist = []
while True:
    word = input('Please type a word: ')
    if word in wordlist:
        print(f'You entered the word {word} twice.Good bye...')
        break
    else:
        wordlist.append(word)