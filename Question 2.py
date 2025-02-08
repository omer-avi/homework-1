#Question 2
sum = 0
i = 1
x = int(input('Please enter a number #1:'))
while x >= 0:
    if x >= 0:
        sum += x
        avg = sum / i
        i += 1
        x = int(input(f'Please enter a number #{i} (avg={int(avg)}. sum={sum}):'))

print('Thank you.Goodbye.')