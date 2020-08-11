import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, ifft

alpha = 2.1
def logistic(alpha, x):
    return alpha * x * (1-x)

def myplots():
    n = 200 #iterations
    pop = list()
    counter = 0
    x = 0.5
    while counter < n:
        pop.append(x)
        x = logistic(alpha, x)
        counter += 1
    plt.plot(range(n), pop, 'b.-')
    plt.xlabel('generations')
    plt.ylabel('population')
    plt.title('alpha = ' + str(alpha))
    plt.show()
    return

if __name__ == '__main__':
    myplots()



