def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res*i
    return res


n = int(input("Enter a number"))
r = fact(n)
print(r)
