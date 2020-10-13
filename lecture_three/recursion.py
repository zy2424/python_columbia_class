def fibonacci(n):
    # the base case
    # there may be more than one of these
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # the recursive case
        # where the function is called again
        # and again, until we get to the base case
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(13)])
# fibonacci(2)
# fibonacci(1) + fibonacci(0) = 1 + 0 => 1

# recursion is just a fancy while loop.
def fib_iterative(n):
    tmp_results = [1, 1]
    counter = 2
    while counter < n:
        tmp_results.append(tmp_results[counter-1] + tmp_results[counter-2])
        counter += 1
    tmp_results = [0] + tmp_results 
    return tmp_results[n]

print([fibonacci(i) == fib_iterative(i) for i in range(13)])
