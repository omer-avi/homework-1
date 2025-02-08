# #Question 1
# x = int(input('Please enter a number:'))
# for i in range(1,x) :
#     if x % i == 0:
#         print(i ,end=',')
#

# #Question 2
# sum = 0
# i = 1
# x = int(input('Please enter a number #1:'))
# while x >= 0:
#     if x >= 0:
#         sum += x
#         avg = sum / i
#         i += 1
#         x = int(input(f'Please enter a number #{i} (avg={int(avg)}. sum={sum}):'))
#
# print('Thank you.Goodbye.')

#Question 3
# wordlist = []
# while True:
#     word = input('Please type a word: ')
#     if word in wordlist:
#         print(f'You entered the word {word} twice.Good bye...')
#         break
#     else:
#         wordlist.append(word)

#Question 4
a_list = []
while True:
    a = input('Enter a list of numbers, when you want to finish entering enter +:')
    if a != '+':
     a_list.append(a)
    else:
        break
b_list = []
while True:
    a = input('Enter a new list of numbers, when you want to finish entering enter +:')
    if a != '+':
     b_list.append(a)
    else:
        break
    b_list.append(a)
a_counter = 0
b_counter = 0
min_length=min(len(a_list),len(b_list)  while True:
        for i in a_list:
            if a_list[i] > b_list[i]:
                a_counter += 1
            else:
                b_counter = + 1
        else:
            break