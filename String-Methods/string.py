a="cat sat on table" 
print(a) #cat sat on table
print(type(a)) #<class 'str'>

b="I'm writting book"
print(b) #I'm writting book


c="Business man"
print(c) #Business man
print(type(c)) #<class 'str'>
print(c[8]) # (output is space)
#print(c[30]) #IndexError: string index out of range


s = "sithamma vakotlo sirimalle chettu"
print(len(s)) #33




#split()
s="twinkle twinklw little star"
print(len(s)) #27
print(s.split()) #['twinkle', 'twinklw', 'little', 'star']
print(s.split("t")) #['', 'winkle ', 'winklw li', '', 'le s', 'ar']
print(s.split("w")) #['t', 'inkle t', 'inkl', ' little star']
print(s.split("nkle")) #['twi', ' twinklw little star']

s="na savi nen sastha nik endhuku"
print(s.split("a",2)) #['n', ' s', 'vi nen sastha nik endhuku']
print(s.split("a",-1)) #['n', ' s', 'vi nen s', 'sth', ' nik endhuku']
print(s.split("a")) #['n', ' s', 'vi nen s', 'sth', ' nik endhuku']


#rsplit()
s="lakshman manchi baludu"
print(s.split()) #['lakshman', 'manchi', 'baludu']
print(s.rsplit()) #['lakshman', 'manchi', 'baludu']
print(s.split("a")) #['l', 'kshm', 'n m', 'nchi b', 'ludu']
print(s.rsplit("a")) #['l', 'kshm', 'n m', 'nchi b', 'ludu']
print(s.split("a",2)) #['l', 'kshm', 'n manchi baludu']
print(s.rsplit("a",2)) #['lakshman m', 'nchi b', 'ludu']

#stip()
s="     hellooo    "
print(len(s)) #16
print(s.strip()) #hellooo
print(len(s.strip())) #7

s1="$$$$$$hellooo$$$$$$$$$"
print(s1.strip("$")) #hellooo

s2="$$$$helloo$$$$world$$$$"
print(s2.strip("$")) #helloo$$$$world

s3="@#$ heloo world @#$"
print(s3.strip("@#$")) #helloo world

#lstrip()
s="     helloo    "
print(s.lstrip()) #hellooo
print(len(s.lstrip())) #10
print(s1.lstrip("$")) #hellooo$$$$$$$$$
print(len(s1.lstrip())) #22
print(s2.lstrip("$")) #helloo$$$$world$$$$
print(len(s2.lstrip())) #23
print(s3.lstrip("@#%")) #$ heloo world @#$
print(len(s3.lstrip())) #19

#rstrip()

s="     helloo    "
print(s.rstrip()) #     helloo
print(len(s.rstrip())) #11
print(s1.rstrip("$")) #$$$$$$hellooo
print(len(s1.rstrip())) #22
print(s2.rstrip("#")) #$$$$helloo$$$$world$$$$
print(len(s2.rstrip())) #23
print(s3.rstrip("@#%")) #@#$ heloo world @#$
print(len(s3.rstrip())) #19

#join()

s="butterfly"
print("_".join(s)) #b_u_t_t_e_r_f_l_y
print(" hi ".join(s)) #b hi u hi t hi t hi e hi r hi f hi l hi y

s= "ganesh idol"
a=s.split()
print(a) #['ganesh', 'idol']
print("_".join(a)) #ganesh_idol

#string with boolean methods
#startswith()
s="do not open the door"
print(s.startswith("d")) #True
print(s.startswith("F")) #False
print(s.startswith("do")) #True

s="shut your mouths"
print(s.startswith("d",5)) #False
print(s.startswith("d",10,99)) #False
print(s.startswith("x",0,19)) #False

#endwith()
s="why kattappa killed bahubali?"
print(s.endswith("?")) #True
print(s.endswith("w")) #False
print(s.endswith("bali?")) #True
print(s.endswith("d",4,-10)) #True
print(s.endswith("?",17,)) #True