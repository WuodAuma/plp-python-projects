a = ["banana", "apple", "mango"]
print(type(a))
a[1] = "orange"
print(a)
for x in a:
    print(x)
b = [x*2 for x in range(1, 6)]
print(b)