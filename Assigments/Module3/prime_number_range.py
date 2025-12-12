"""
    **Prime Number Range**: İki sayı arasındaki tüm asal sayıları bulan program
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers(num1, num2):
    for i in range(num1, num2+1):
        if is_prime(i):
            print(i, end=" ")

if __name__ == "__main__":
    prime_numbers(1, 100)
