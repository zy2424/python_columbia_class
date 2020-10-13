def function_one(x):
    x += 1
    # return passes variables or objects
    # back to global scope
    return x

def function_two(y):
    y += 1
    # if functions do not have a return
    # then they will not pass anything back to
    # global scope, by default!!!

    
x = 9
result_one = function_one(x)
print(result_one) #result = 10 
y = 9
result_two = function_two(y)
print(result_two) #result = None

