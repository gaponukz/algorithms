import matplotlib.pyplot as plt
import numpy

def lagrange_polynomial(*points):
    def function(x):
        y = 0

        for i in range(len(points)):
            poly = 1

            for j in range(len(points)):
                if i != j:
                    poly *= (x - points[j][0])/(points[i][0] - points[j][0])
        
            y += poly * points[i][1]
        
        return y
    
    return function

def derivative(function, point, e=1e-3):
    return (function(point + e) - function(point)) / e

if __name__ == '__main__':
    f = lagrange_polynomial((1, 1), (2, 4), (3, 9))
    x = numpy.linspace(-5,5,100)

    y = f(x)
    dx = derivative(f, x)
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y)
    plt.plot(x, dx)

    plt.show()
