# import numpy as np
import math

def const_iter_gen(value):
    while 1:
        yield value

def log_normal(x,avg=0,std=1):
    return math.exp(-(math.log(x)-avg)**2/(2*std**2))/(x*std*math.sqrt(2*math.pi))

if __name__ == "__main__":
    # test ---------------------------------------------------------- #
    import numpy as np
    import matplotlib.pyplot as plt
    # log normal
    x=np.linspace(0,50,5001)[1::]
    y=list(map(log_normal,x,const_iter_gen(1),const_iter_gen(1)))
    # plt.bar(x,y)
    plt.plot(x,y)
    plt.show()