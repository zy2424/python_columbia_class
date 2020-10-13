def function(x, y, z):
    x += 1
    y += 1
    z += 1
    return x, y, z

one = 1
two = 2
three = 3
# one goes to x
# two goes to y
# three goes z
result_one, result_two, result_three = function(
    one, two, three
)
# x goes to result_one
# y goes to result_two
# z goes to result_three
print(result_one, result_two, result_three)
result_of_print = print("blah blah blah")
print(result_of_print)
