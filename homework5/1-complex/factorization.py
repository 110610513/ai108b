x = int(input("Number to factorize: "))

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
            print(i)

fn = factors.copy()

for i in range(len(fn) - 1):
    cur = fn[i]
    nxt = fn[i + 1]
    if cur == nxt:
        cons *= cur
        fn[i] = fn[i + 1] = 0

for i in fn:
    if i:
        rs *= i

print("rs: ", rs)
print("cons: ", cons)
print("factors: ", factors)