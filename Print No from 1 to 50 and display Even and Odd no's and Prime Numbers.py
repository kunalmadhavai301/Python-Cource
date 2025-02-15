Develop a code in python using while and if to display 1 to 50 numbers satisfy following conditions
1. If number is divisible by 2 then its even and not then its odd one.
2. Display the prime numbers as well (eg. 17 is odd and prime as well).
Output should be like as follows-
1 - odd and prime
2 - even prime
3 - odd prime
4- even
5 - odd prime
6 - even
7 - odd prime and so on




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 51):
    status = "even" if num % 2 == 0 else "odd"
    if is_prime(num):
        status += " prime"
    print(f"{num} {status}")
