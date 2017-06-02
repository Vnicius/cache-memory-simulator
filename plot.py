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

    plt.title("Memoria Cache (RAM:8000 e Cache:100)")
    plt.xlabel("Numero de calls")
    plt.ylabel("Taxa de cache hit")
    plt.plot(x.pop(0),y.pop(0), x.pop(0),y.pop(0))
    plt.legend(['Direct Map', 'Associative Map'], loc='best')
    plt.savefig("teste.png")

    #plt.title("C++")
    #plt.xlabel("Nível de entropia (%)")
    #plt.ylabel("Tempo médio (ms)")
    #plt.plot(x.pop(0),y.pop(0))
    #plt.legend(['C++ sort'], loc='best')
    #plt.savefig("c++-1kk.png")



plot()
