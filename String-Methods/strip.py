# strip()

s = "     hellooo    "
print(len(s))  # 16
print(s.strip())  # hellooo
print(len(s.strip()))  # 7

s1 = "$$$$$$hellooo$$$$$$$$$"
print(s1.strip("$"))  # hellooo

s2 = "$$$$helloo$$$$world$$$$"
print(s2.strip("$"))  # helloo$$$$world

s3 = "@#$ heloo world @#$"
print(s3.strip("@#$"))  # heloo world