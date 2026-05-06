fruits = ["apple", "banana", "orange"]
numbers = (1, 2, 3, 4, 5)
mixed = ("hello", 42, 3.14, True)
empty_list = []


print(fruits[0])
print(fruits[1])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

fruits.append("kiwi")
fruits.insert(1, "grape")
fruits.remove("banana")
popped_fruit = fruits.pop()
fruits.sort()
fruits.reverse()

len(fruits)
"apple" in fruits
fruits + ["mango"]
fruits * 2

print(fruits)