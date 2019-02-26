from random import randint

numbers = [i for i in range(1,101)]

random_list = []

for index in range(0,100):
    print(index)
    number = numbers[randint(0,len(numbers)-1)]
    random_list.append(number)
    numbers.remove(number)

print(random_list)
