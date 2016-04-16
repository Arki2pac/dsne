from decimal import Decimal

def doWhile():
    while True:
        func1()
        if not (cond1() or cond2() or cond3()):
            break
def doWhile2():
    while True:
        func2()
        if not (cond1() or cond2()):
            break

C = 0.01
Epsilon = 0.00001
X = 1.00
Y = 2.00
Z = 1.00
Xnew = 1.00
Ynew = 2.00
Znew = 1.00
Wynik = 1.00

def func1():
    global X,Y,Z,Xnew,Ynew,Znew
    X = Xnew
    Y = Ynew
    Z = Znew
    Xnew = X - C * (4 * X - 2 * Y - 2)
    Ynew = Y - C * (4 * Y - 2 * X - 2 * Z)
    Znew = Z - C * (2 * Z - 2 * Y)

def cond1():
    global X,Xnew
    return bool(abs(Xnew - X) > Epsilon)
def cond2():
    global Y,Ynew
    return bool(abs(Ynew - Y) > Epsilon)
def cond3():
    global Z,Znew
    return bool(abs(Znew - Z) > Epsilon)

doWhile()

Wynik = 2 * Xnew * Xnew + 2 * Ynew * Ynew + Znew * Znew - 2 * Xnew * Ynew - 2 * Ynew * Znew - 2 * Xnew + 3

print("Funkcja 1:")
print("f(X,Y,Z) = " + str(Wynik))
print("X = " + str(Xnew))
print("Y = " + str(Ynew))
print("Z = " + str(Znew) + "\n")

Xnew = 4
Ynew = 4

#########################################################

def func2():
    global X,Y,Xnew,Ynew
    X = Xnew
    Y = Ynew
    Xnew = X - C * (12 * X * X * X + 12 * X * X - 24 * X)
    Ynew = Y - C * (24 * Y - 24)


doWhile2()
Wynik = 3 * Xnew * Xnew * Xnew * Xnew + 4 * Xnew * Xnew * Xnew - 12 * Xnew * Xnew + 12 * Ynew * Ynew - 24 * Ynew

print("Funkcja 2:")
print("f(X,Y) = " + str(Wynik))
print("X = " + str(Xnew))
print("Y = " + str(Ynew))
