import math, cmath

def simp(x):
    cons = 1
    rs = 1
    primes = [2, 3, 5, 7, 11, 13]
    factors = []

    for i in primes:
        if not x % i:
            while x >= 1:
                if(x % i) != 0:
                    break
                x /= i
                factors.append(i)

    for i in range(len(factors) - 1):
        cur = factors[i]
        nxt = factors[i + 1]
        if cur == nxt:
            cons *= cur
            factors[i] = factors[i + 1] = 0

    for i in factors:
        if i:
            rs *= i
    return cons, rs

def root2(a,b,c):
    t = b*b - 4*a*c
    if (t < 0):
        # t2 = cmath.sqrt(t)
        # return [(-b+t2)/(2*a), (-b-t2)/(2*a)]
        t *= -1
        cons, rs = simp(t)

        ans1 = '(' + str(-b) + '+' + str(cons) + 'i*' + str(rs) + '^(1/2))/' + str(2*a)
        ans2 = '(' + str(-b) + '-' + str(cons) + 'i*' + str(rs) + '^(1/2))/' + str(2*a)
        return ans1, ans2

    t2 = math.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of 1x^2+4x+0= ", root2(1, 4, 0))
print("root of 1x^2+2x+3= ", root2(1, 2, 3))
