# startswith()

s = "do not open the door"

print(s.startswith("d"))  # True
print(s.startswith("F"))  # False
print(s.startswith("do"))  # True

s = "shut your mouths"

print(s.startswith("d", 5))  # False
print(s.startswith("d", 10, 99))  # False
print(s.startswith("x", 0, 19))  # False