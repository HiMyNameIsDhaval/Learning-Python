# List

print('List')
fruit = ['Apple', 'Litchee']

fruit[0] = 'Mango'
print(fruit)

#Duplicate

numbers = [1,3,2,4,3,2]
print(numbers)
print(numbers.index(3))
print(numbers.count(3))
print(type(numbers))

# Tuple 
# Unchangeable
print('Tuples')

fruit = ('Apple', 'Litchee')

# fruit[0] = 'Mango'
print(fruit)

# Construstor
# numbers = tuple((1,3,2,4,3,2))

numbers = (1,3,2,4,3,2,)


print(numbers)
print(len(numbers))
print(type(numbers))

print(numbers.count(3))

print(numbers.index(3))

# Sets
print('Sets')

# Unordered
# Unindexed
# Unchangable*

number = {1,2,3,4,5}
print(number)
print(len(number))
print(type(number))

number.remove(5)
print(number)
print(len(number))
print(type(number))

number.add(5)
print(number)
print(len(number))
print(type(number))

number.add(6)
print(number)
print(len(number))
print(type(number))

# No Dublicates

number.add(1)
print(number)




