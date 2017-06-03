# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import sys

def plot():
    file = open(sys.argv[1],"r")
    x = []
    y = []
    x_temp = []
    y_temp = []
    i = 1

    for line in file:
        tmp = line.split()
        x_temp.append(int(tmp.pop(0)))
        y_temp.append(int(tmp.pop(0)))
        if i % 3 == 0:
            x.append(x_temp)
            y.append(y_temp)
            x_temp = []
            y_temp = []
        i += 1

    plt.title("Memoria Cache (RAM:"+sys.argv[3]+" e Cache:"+sys.argv[4]+")")
    plt.xlabel("Numero de calls")
    plt.ylabel("Taxa de cache hit")
    plt.plot(x.pop(0),y.pop(0), x.pop(0),y.pop(0), x.pop(0),y.pop(0), x.pop(0),y.pop(0))
    plt.legend(['Direct Map', 'Associative Map', 'Associative Map - 2 way', 'Associative Map - 4 way'], loc='best')
    plt.savefig(sys.argv[2]+".png")

plot()
