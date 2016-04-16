def printmodel(F,n):
    i = 0
    line = ''
    for i in range(n):
        if (i % 5 == 0) and (i != 0):
            print line+"\n"
            line =''
        if F[i] == -1:
            line += " - "
        else:
            line += " * "
        if (i+1 == n):
            print line+"\n"

def sgn(FZ,W,Z1,n):
    wynik = 0.0
    for i in range(n):
        for j in range(n):
            wynik = wynik + W[i][j] * Z1[j]
            FZ[i] += wynik
            wynik = 0.0

    for i in range(n):
        if FZ[i] > 0:
            FZ[i] = 1
        else:
            FZ[i] = -1

def multiplyvector(W,Z0,Z1,n):
    for i in range(n):
        for j in range(n):
            W[i][j] = ((Z0[i]*Z0[j])/n) + ((Z1[i]*Z1[j])/n)
n = 25
wielkosc = 25
W = [ [ 0.0 for i in range(n) ] for j in range(n) ]
W1 = [ [ 0.0 for i in range(n) ] for j in range(n) ]


Z0 = [-1.0, -1.0, -1.0, -1.0, -1.0,
       -1.0, 1.0, 1.0, 1.0, -1.0,
       -1.0, 1.0, -1.0, 1.0, -1.0,
       -1.0, 1.0, 1.0, 1.0, -1.0,
       -1.0, -1.0, -1.0, -1.0, -1.0]

Z1 = [-1.0, -1.0, -1.0, -1.0, -1.0,
        -1.0, 1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, -1.0, -1.0, -1.0 ]

Z0z = [-1.0, 1.0, 1.0, 1.0, -1.0,
        -1.0, 1.0, -1.0, 1.0, -1.0,
        -1.0, 1.0, -1.0, 1.0, -1.0,
        -1.0, 1.0, 1.0, 1.0, -1.0,
        -1.0, -1.0, -1.0, -1.0, -1.0]

Z1z = [-1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0,
        -1.0, -1.0, 1.0, -1.0, -1.0]

print "Z0:"+"\n"
printmodel(Z0,n)
print "Z1:"+"\n"
printmodel(Z1,n)



FZ0 = [ 0.0 for i in range(n) ]
FZ1 = [ 0.0 for i in range(n) ]
FZ0z = [ 0.0 for i in range(n) ]
FZ1z = [ 0.0 for i in range(n) ]

# SGN
multiplyvector(W,Z0,Z1,n)

print "\n\n SGN(W*Z0) = \n"

sgn(FZ0,W,Z0,n)
printmodel(FZ0,n)

print "\n\n SGN(W*Z1) = \n"

sgn(FZ1,W,Z1,n)
printmodel(FZ1,n)


print "Zaburzenie 0 ':"+"\n"
printmodel(Z0z,n)
print "Zaburzenie 1':"+"\n"
printmodel(Z1z,n)

multiplyvector(W1,Z0z,Z1z,n)

print "\n\n SGN(W * Z0' - Zaburzone = \n"

sgn(FZ0z,W,Z0z,n)
printmodel(FZ0z,n)

print "\n\n SGN(W * Z1' - Zaburzone  = \n"

sgn(FZ1z,W,Z1z,n)
printmodel(FZ1z,n)
