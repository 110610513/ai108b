from sympy import exp
v0 = int(input("V0(V): "))
r = int(input("Resistor(kΩ): "))
c = int(input("Capacitor(μF): "))

rc = (r * 10**3) * (c * 10**(-6))

print(r, c)

def rcV(v0, t):
    if t >= 5:
        return 0

    return float(v0 * exp(-t))

print("T = ", rc)
for i in range(7):
    vc = round(rcV(v0, i), 3)
    ci = round(vc/r, 3)
    print("t = {}:".format(i))
    print("Vc = " + str(vc) + " V, i = " + str(ci) + " mA")
