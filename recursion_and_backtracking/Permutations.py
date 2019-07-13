def permutations(S):
    soFar = []
    B = S
    for perm in genPerms(soFar, B):
        print(perm)


def genPerms(soFar, B):
    if len(B) == 0:
        yield soFar
    else:
        for x in range(0, len(B)):
            for perm in genPerms(soFar + [B[x]], B[0:x] + B[x+1:]):
                yield perm


permutations(['A', 'B', 'C', 'A'])
