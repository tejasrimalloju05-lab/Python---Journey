# lstrip()

s = "     helloo    "
print(s.lstrip())  # helloo
print(len(s.lstrip()))  # 10

s1 = "$$$$$$hellooo$$$$$$$$$"
print(s1.lstrip("$"))  # hellooo$$$$$$$$$

print(len(s1.lstrip("$")))  # 22

s2 = "$$$$helloo$$$$world$$$$"
print(s2.lstrip("$"))  # helloo$$$$world$$$$
print(len(s2.lstrip("$")))  # 23

s3 = "@#$ heloo world @#$"
print(s3.lstrip("@#%"))  # $ heloo world @#$
print(len(s3.lstrip("@#%")))  # 19