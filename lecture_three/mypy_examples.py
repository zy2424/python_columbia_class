#integer - int
#floats - float
#booleans - bool
#strings - str

def function(x: int, y: float, z: str) -> bool:
    number_of_characters = int(x * y)
    return len(z * number_of_characters) < 1700

print(function(1, 1.7451, "a"))
