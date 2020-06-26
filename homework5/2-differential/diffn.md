# Trigonometric differentiation

## Executed result
```
> py .\diffn.py
dft(sin, pi/4)=  0.7071067811864697
dftn(sin, 0 pi/4)=  0.7071067811865476
dftn(sin, 1 pi/4)=  0.7071067811864697
dftn(sin, 2 pi/4)=  -0.7071067811864697
dftn(sin, 3 pi/4)=  -0.7071067811864697
dftn(sin, 4 pi/4)=  0.7071067811864697
dftn(sin, 5 pi/4)=  0.7071067811864697
dftn(sin, 6 pi/4)=  -0.7071067811864697
dftn(sin, 7 pi/4)=  -0.7071067811864697
dftn(sin, 8 pi/4)=  0.7071067811864697
dftn(sin, 9 pi/4)=  0.7071067811864697
```

## Use function dft(f, x, sign) instead of df(f, x, h=step)
dft(f, x, sign) is used to differentiate trigonometric function\
but only with sin(x) and cos(x)
```
```
\
for the differentiation of sin(x) snd(x):
```
sin'(x) = cos(x)
cos'(x) = -sin(x)
```
\
In dft(f, x, sign), f is the corresponding function sin(x) or cos(x)\
and sign is to determine whether the function is positive or negative\
The function retuens 3 values:\
answer in float, current trigonometric function type and the answer sign\
code written in python:
```py
def dft(f, x, sign):
    c = df(x) * f(x)/sin(x) if f == sin else df(x) * f(x)/cos(x)

    ans = [(c * cos(x), cos, 1), (c * -cos(x), cos, -1), 
           (c * -sin(x), sin, -1), (c * sin(x), sin, 1)]
    
    if f == sin:
        return ans[0] if sign == 1 else ans[1]
        
    if f == cos:
        return ans[2] if sign == 1 else ans[3]
```
\
If we want to differentiate a trigonometric function n times\
we add a function dftn(f, x, sign, n), which makes n times differentiation
```py
def dftn(f, x, sign, n):
    if (n == 0):
        return sin(x), sin, 1

    if (n == 1):
        return dft(f, x, sign)
        
    if f == sin:
        return dftn(cos, x, sign, n-1)

    if f == cos:
        return dftn(sin, x, -sign, n-1)
```
