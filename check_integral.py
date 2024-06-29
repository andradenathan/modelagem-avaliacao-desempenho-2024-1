from math import tan, pi
from random import uniform

def check_integral_simulation(N):
    result = 0
    for _ in range(N):
        x = uniform(0, pi/2)
        y = uniform(0, 1)
        if y <= x / tan(x):
            result += 1
    
    return (result/N) * (pi/2)
    
if __name__ == '__main__':
    check_integral_simulation(10 ** 7)