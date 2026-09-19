# split()

s = "twinkle twinklw little star"
print(len(s))  # 27
print(s.split())  # ['twinkle', 'twinklw', 'little', 'star']
print(s.split("t"))  # ['', 'winkle ', 'winklw li', '', 'le s', 'ar']
print(s.split("w"))  # ['t', 'inkle t', 'inkl', ' little star']
print(s.split("nkle"))  # ['twi', ' twinklw little star']

s = "na savi nen sastha nik endhuku"
print(s.split("a", 2))  # ['n', ' s', 'vi nen sastha nik endhuku']
print(s.split("a", -1))  # ['n', ' s', 'vi nen s', 'sth', ' nik endhuku']
print(s.split("a"))  # ['n', ' s', 'vi nen s', 'sth', ' nik endhuku']