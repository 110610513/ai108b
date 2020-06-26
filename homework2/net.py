class Node:
    def __init__(self, v = 0, g = 0):
        self.v = v 
        self.g = g 

    def __str__(self):
        return 'v:{self.v} g:{self.g}'.format(self=self)

class Gate:
    def __init__(self, o, x, y, f, gfx, gfy):
        self.o = o
        self.x = x
        self.y = y
        self.f = f
        self.gfx = gfx
        self.gfy = gfy

    def forward(self):
        self.o.v = self.f(self.x.v, self.y.v)
        return self.o.v

    def backward(self):
        x, y, o, gfx, gfy = self.x, self.y, self.o, self.gfx, self.gfy
        x.g += gfx(x.v,y.v) * o.g
        y.g += gfy(x.v,y.v) * o.g

    def adjust(self, step=0.001): 
        x, y = self.x, self.y
        x.v -= step*x.g
        y.v -= step*y.g
        x.g = 0
        y.g = 0

class Net:
    def __init__ (self):
        self.gates = []

    def variable (self, v, g=0):
        return Node(v, g)

    def op (self, x, y, f, gfx, gfy):
        o = Node()
        g = Gate(o, x, y, f, gfx, gfy)
        self.gates.append(g)
        self.o = o
        return o

    def add (self, x, y):
        return self.op(x, y, lambda x,y:x+y, lambda x,y:1, lambda x,y:1) 
    def mul (self, x, y):
        return self.op(x, y, lambda x,y:x*y, lambda x,y:y, lambda x,y:x) 

    def forward(self): 
        for gate in self.gates:
            gate.forward()
        return self.o.v

    def backward(self):  
        self.o.g = 1 
        for gate in reversed(self.gates): 
            gate.backward()

    def adjust(self, step=0.01): 
        for gate in self.gates:
            gate.adjust(step)

    
    def gradient_descendent (self, maxLoops=100, dumpPeriod=1, step=0.01):
        for loop in range(maxLoops):
            energy = self.forward()
            if loop % dumpPeriod==0:
                print(loop, ' => ', energy)
            self.backward()
            self.adjust(step)

