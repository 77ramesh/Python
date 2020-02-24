import random

'''random class will choose number from given list'''
print(random.choice([3, 5, 1, 9, 7, 8, 4]))

list = [4, 5, 6, 1, 9, 8, 0]

'''list can be passed as argument also'''
print(random.choice(list))

'''random will be generated between 1 to 50, after generating num it will add any given number (4) to it'''
print(random.randrange(1, 50, 4))

print("\nUsing for loop")
'''generating random numbers using for loop'''
for i in range(1, 10):
    print(random.randrange(1, 100))


print("\n Using while loop")
i = 1
while i < 10:
    print(random.randrange(1, 100))
    i+=1


set = (5, 6, 7, 8, 9, 1, 2, 3, 4)

print("Random int using set: ", random.choice(set))

'''print random string using random class'''
persons = ["Ramesh", "Hello", "World", "Python", "Java"]
print(random.choice(persons))
