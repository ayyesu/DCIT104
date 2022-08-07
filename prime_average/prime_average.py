# Using a range of 1 to 100;

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

    
def average_primes(num):
    sum = 0
    count = 0
    for i in range(1, num):
        if is_prime(i):
            sum += i
            count += 1
    return sum/count

average = average_primes(100)
print("The average sum of all prime numbers between 1 and 100 is: ", average)