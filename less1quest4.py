a = int(input("enter value: "))
num = a%10
while a>0:
    if (a%10 > num):
        num = a % 10
    a = a//10

print(num)