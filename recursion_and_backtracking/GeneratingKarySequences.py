def possibilities(k):
    result = []
    for i in range(0,k):
        result.append(str(i))
    return result


def base_k_strings(n,k):
    if n ==0:
        return []
    if n ==1:
        return possibilities(k)
    return [digit + sequence for digit in possibilities(k) for sequence in base_k_strings(n-1,k)]


print(possibilities(4))
print(base_k_strings(2,4))
