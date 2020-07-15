a = float(input("enter value1: "))
b = float(input("enter value2: "))
i = 1
while True:
    print(f"day: {i} dist {a}")
    if(a>b):
        break
    a *= 1.1
    i += 1
print(i)