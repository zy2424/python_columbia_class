def is_prime(integer):
    prime_number = True
    for i in range(1, integer//2):
        if integer % i == 0:
            prime_number = False
    return prime_number

print([i
 for i in range(1,100)
 if is_prime(i)
])
