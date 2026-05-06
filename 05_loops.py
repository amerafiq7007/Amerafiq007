# For loop 
# for i in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)
# while loop 
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# Loop control statment
# for i in range(10):
#     if i == 3:
#         continue
#     if i == 7:
#         break
#     print(i)

# Nasted loop
# for i in range(2):
#     for j in range(3):
#         print(f"({i}, {j})")


# #Exercise 
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

limit = 20

for num in range(3, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)




def multiplication_table(num, limit=10):
    table = [f"{num:2} x {i:2} = {num*i:3}" for i in range(1, limit+1)]
    print("\n".join(table))

multiplication_table(7)




def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

limit = 20
primes = [n for n in range(2, limit+1) if is_prime(n)]

print("Prime numbers:", primes)





limit = 20

print(f"Prime numbers from 1 to {limit}:")
print("-" * 30)

for num in range(2, limit+1):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(f"✔ {num}")




        