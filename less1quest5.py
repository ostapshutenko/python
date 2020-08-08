a = float(input("enter value1: "))
b = float(input("enter value2: "))

if (a>b):
    n = ((a-b)*100/a)
    print(f"прибыль, {n} процентов")
elif a==b:
    print("равновесие")
else:
    print("убыток")

c = int(input("enter value peoples: "))
print(((a-b)/c))
