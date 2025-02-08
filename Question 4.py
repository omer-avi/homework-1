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

a_counter = 0
b_counter = 0
min_length = min(len(a_list),len(b_list))
for i in range(min_length):
    if a_list[i] > b_list[i]:
         a_counter += 1
    elif b_list[i] > a_list[i]:
           b_counter += 1

if a_counter > b_counter:
    print(a_list)
elif a_counter != b_counter:
    print(b_list)
else:
    print('There is an equal amount in both lists.')

