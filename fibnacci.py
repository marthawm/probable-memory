def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        x = a
        a = b
        b = x + b
    return a
y = int(raw_input("enter terms:"))
for item in range(y):
    print fibonacci(item)
