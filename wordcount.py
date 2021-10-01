S = 'I want that Farm House to be in my name, comprende? Also, I want Chocolates.'
D = {}
#SS = S.split()
for item in S:
    if item in D:
        D[item] = D[item] + 1
    else:
        D[item] = 1

print(D)
