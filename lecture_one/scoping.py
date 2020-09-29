switch = 17
if switch % 2 == 0:
    x = switch
    print("is even")
elif switch % 3 == 0:
    y = "boya"
    print("is divisible by three")
else:
    z = "smart"
    print("is not divisible by 2 or 3")

print([elem for elem in locals() if "_" not in elem])

