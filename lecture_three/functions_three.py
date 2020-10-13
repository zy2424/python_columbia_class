def add(x, y):
    # functions unlike if else
    # are unaware of other variables
    # outside of their scope
    # one += two - fails
    return x + y


one, two = 1, 2
print(add(one, two))
