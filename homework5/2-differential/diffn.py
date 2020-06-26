from math import sin, cos, pi

def df(x, h=0.0001):
    return (x+h-x)/(h)

def dft(f, x, sign):
    c = df(x) * f(x)/sin(x) if f == sin else df(x) * f(x)/cos(x)

    ans = [(c * cos(x), cos, 1), (c * -cos(x), cos, -1), 
           (c * -sin(x), sin, -1), (c * sin(x), sin, 1)]
    
    if f == sin:
        return ans[0] if sign == 1 else ans[1]
        
    if f == cos:
        return ans[2] if sign == 1 else ans[3]

def dftn(f, x, sign, n):
    if (n == 0):
        return sin(x), sin, 1

    if (n == 1):
        return dft(f, x, sign)
        
    if f == sin:
        return dftn(cos, x, sign, n-1)

    if f == cos:
        return dftn(sin, x, -sign, n-1)

x = pi/4

print("dft(sin, pi/4)= ", dft(sin, x, 1)[0])

for i in range(10):
    ans, f, sign = dftn(sin, x, 1, i)
    print('dftn(sin,', i, 'pi/4)= ', ans)
