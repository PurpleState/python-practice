B=['A', 'B', 'C', 'A']
#for x in range(0, len(B)):
    #print([B[x]])
for x in range(0, len(B)):
    print(B[0:x])
for x in range(0, len(B)):
    print(B[x + 1:])
for x in range(0, len(B)):
    print(B[0:x] + B[x+1:])
