# def adds_one(x):
#     x += 1
#     return x

def adds_one(x):
    return x + 1

z = 0
for _ in range(100):
    z = adds_one(z)
    
print(z)
