import sys
if len(sys.argv) != 2 or len(sys.argv[1]) != 26:
print("Plz read the instruction and do it agian")
sys.exit(0)
upper = sys.argv[1].upper()
lower = sys.argv[1].lower()
p = "abcdefghijklmnopqrstuvwxyz"
P = p.upper()
n = input("Plain text:")
print("Encrypted: ", end = "")
for i in n:
flag = i.isupper()
if i == " " or i in "1234567890":  
print(i, end = "")
else:
if i in p:
a = p.find(i)
else:
a = P.find(i)
if flag:
print(upper[a % 26], end = "")
else:
print(lower[a % 26], end = "")