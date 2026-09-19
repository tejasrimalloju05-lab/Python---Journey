# rsplit()

s = "lakshman manchi baludu"

print(s.split())  # ['lakshman', 'manchi', 'baludu']
print(s.rsplit())  # ['lakshman', 'manchi', 'baludu']

print(s.split("a"))  # ['l', 'kshm', 'n m', 'nchi b', 'ludu']
print(s.rsplit("a"))  # ['l', 'kshm', 'n m', 'nchi b', 'ludu']

print(s.split("a", 2))  # ['l', 'kshm', 'n manchi baludu']
print(s.rsplit("a", 2))  # ['lakshman m', 'nchi b', 'ludu']