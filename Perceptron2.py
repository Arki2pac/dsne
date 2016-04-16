from numpy import array, zeros, ones

data = array([
    array([
        0,0,0,0,0,
        0,1,1,0,0,
        0,0,1,0,0,
        0,0,1,0,0,
        0,0,1,0,0,1]),
    array([
        0,0,1,1,0,
        0,0,0,1,0,
        0,0,0,1,0,
        0,0,0,0,0,
        0,0,0,0,0,1]),
    array([
        0,0,0,0,0,
        1,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,
        0,1,0,0,0,1]),
    array([
        0,0,0,0,0,
        0,1,1,1,0,
        0,1,0,1,0,
        0,1,1,1,0,
        0,0,0,0,0,1]),
    array([
        0,0,0,0,0,
        0,0,0,0,0,
        1,1,1,0,0,
        1,0,1,0,0,
        1,1,1,0,0,1])
])

def dot(w, u):
    output = 0
    for i in xrange(26):
        output += w[i] * u[i]

    if output >= 0:
        return 1
    else:
        return 0

class perceptron(object):
    def __init__(self, c, epochs):
        self.w_ = ones(26)
        self.c_ = c
        self.epochs_ = epochs

    def train(self, data):
        t = 0
        counter = 0
        z = 0
        y = 0
        while counter < self.epochs_:

            u = data[t%self.epochs_]
            y = dot(self.w_, u)

            if t%self.epochs_+1 <= 3:
                z = 1
            else:
                z = 0

            for i in xrange(26):
                self.w_[i] = self.w_[i] + self.c_ * (z - y) * u[i]

            t += 1
            if(y == z):
                counter += 1
            else:
                counter = 0

        print(t)
        print(self.w_)

if __name__ == '__main__':
    p1 = perceptron(1.0, 5)
    p2 = perceptron(0.1, 5)
    p3 = perceptron(0.01, 5)

    print("p1")
    p1.train(data)
    print("p2")
    p2.train(data)
    print("p3")
    p3.train(data)