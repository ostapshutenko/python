a = int(input("type tyme"))
second = a % 60

a = int(a/60)

minutes = a%60

a = int(a/60)

hour = a

print(f"{hour}:{minutes}:{second}")