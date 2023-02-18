
number = int(input('Enter the number: '))
divisors = [n for n in range(1, 101)]
results = []


for i in range(len(divisors)):
    if (number % divisors[i] == 0):
        results.append(divisors[i])
    else:
        pass

def prime_number():
    if len(results) > 2:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number") 
prime_number()