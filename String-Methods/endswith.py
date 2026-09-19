# endswith()

s = "why kattappa killed bahubali?"

print(s.endswith("?"))  # True
print(s.endswith("w"))  # False
print(s.endswith("bali?"))  # True
print(s.endswith("d", 4, -10))  # True
print(s.endswith("?", 17))  # True