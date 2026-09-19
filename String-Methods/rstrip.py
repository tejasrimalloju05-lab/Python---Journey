# rstrip()

s = "     helloo    "
print(s.rstrip())  #      helloo
print(len(s.rstrip()))  # 11

s1 = "$$$$$$hellooo$$$$$$$$$"
print(s1.rstrip("$"))  # $$$$$$hellooo
print(len(s1.rstrip("$")))  # 22

s2 = "$$$$helloo$$$$world$$$$"
print(s2.rstrip("#"))  # $$$$helloo$$$$world$$$$
print(len(s2.rstrip("#")))  # 23

s3 = "@#$ heloo world @#$"
print(s3.rstrip("@#%"))  # @#$ heloo world @#$
print(len(s3.rstrip("@#%")))  # 19