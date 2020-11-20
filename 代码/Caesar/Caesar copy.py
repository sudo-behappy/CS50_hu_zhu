import sys
if len(sys.argv) != 2:
print("Plz read the instruction and do it agian")
sys.exit(0)
p = "abcdefghijklmnopqrstuvwxyz" 
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = input("Plain text:")
print("Encrypted: ", end = "")
for i in n:
if i == " " or i in "1234567890":  
print(i, end = "")
else:
if i in p:
a = p.find(i)
else:
a = P.find(i)
print(p[(a + int(sys.argv[1])) % 26], end = "")