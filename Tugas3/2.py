def extended_euclid(a,b):

    if a%b == 0:
        return [0,1]

    [u,v] = extended_euclid(b,a%b)
    q = (a - a % b) / b
    return [v,u-v*q]

print(extended_euclid(26513, 32321))