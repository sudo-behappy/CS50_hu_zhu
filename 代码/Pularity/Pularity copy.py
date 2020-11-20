import sys
def find(input:str, target, init:int):
    for i in range(init, len(input)):
        if input[i] == target:
            return i 
    return -1
if len(sys.argv) < 2:
    print("plz read the instruction and do it again")
    sys.exit(0)
num = int(input("number of voters:"))
aGoodName = [0] * num
flag = 0
for i in range(0, num):
    t = input("You vote:")
    aGoodName[find(sys.argv, t, 1) - 1] += 1
print("the winner is: ",sys.argv[find(aGoodName, max(aGoodName), 0) + 1])
