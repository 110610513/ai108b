# Find root

## Executed result
```
>py .\root.py 
root of 1x^2+4x+0=  [0.0, -4.0]
root of 1x^2+2x+3=  ('(-2+2i*2^(1/2))/2', '(-2-2i*2^(1/2))/2')
```

## Add function simp(x)
simp(x) is used to simplifying a square root
```
```
\
First,  make a prime factorization\
Assumes that our number can be factorized under the prime numbers below:\
primes = [2, 3, 5, 7, 11, 13]\
Then makes a list to store factors and we can do the factorization
```py
primes = [2, 3, 5, 7, 11, 13]
factors = []

for i in primes:
    if not x % i:
        while x >= 1:
            if(x % i) != 0:
                break
            x /= i
            factors.append(i)
```
\
Second, do the factorization\
fetch every 2 numbers and multiply into cons if they are equivalent\
and the rest numbers was not been fetched will be left in radical
```py
cons = 1
rs = 1
for i in range(len(factors) - 1):
    cur = factors[i]
    nxt = factors[i + 1]
    if cur == nxt:
        cons *= cur
        factors[i] = factors[i + 1] = 0

for i in factors:
    if i:
        rs *= i
```

## If the roots are complex numbers
For the variable t is the number calculated after discriminant quadratic formula: b^2−4ac
```
```
\
First, makes t positive so it can be factorized easier\
after simp(t) we get a radical constant and a surd
```py
t *= -1
cons, rs = simp(t)
```
\
Second, generates the answer\
because t is already smaller than 0 so we know that the root is definitely a complex number\
there we add i as the imaginary number in complex number\
then it returns the root
```py
ans1 = '(' + str(-b) + '+' + str(cons) + 'i*' + str(rs) + '^(1/2))/' + str(2*a)
ans2 = '(' + str(-b) + '-' + str(cons) + 'i*' + str(rs) + '^(1/2))/' + str(2*a)
return ans1, ans2
```

## cmath
Or just import cmath\
which helps handle complex numbers
```py
t2 = cmath.sqrt(t)
```
