#Question 1
x = int(input('Please enter a number:'))
for i in range(1,x) :
    if x % i == 0:
        print(i ,end=',')
