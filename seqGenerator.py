#!/usr/bin/python3
#-*- coding : utf-8 -*-
import random
import sys

tamMax = int(sys.argv[1])
i = 1
numCalls = int(sys.argv[2])
actual = 0
isLoop = True if sys.argv[3].lower() == "true" else False

if isLoop:
    # loops
    out = open("assets/loop/"+sys.argv[2]+".in","w")
    out.write(str(actual)+"\n")
    loop = [0]
    maxLoop = 100

    while i < numCalls:
        rNum = random.randint(0,100)
        #loop
        if rNum > 95:
            loopCount = random.randint(1, len(loop))

            if (loopCount + len(loop)) > numCalls:
                loopCount = numCalls - len(loop) - 2
            elif loopCount > maxLoop:
                loopCount = maxLoop

            for v in loop[len(loop)-loopCount-1:]:
                out.write(str(v)+"\n")
                loop.append(v)

            actual = loop[-1]
            i = len(loop)
            continue
        #jump
        elif rNum > 80:
            actual = random.randint(0,tamMax - 1)
            loop.append(actual)
        else:
            actual = (actual + 1) % (tamMax - 1)
            loop.append(actual)

        out.write(str(actual)+"\n")
        i += 1

    # print(len(loop))
    # for value in loop:
    #     out.write(str(value)+"\n")
else:
    out = open("assets/jmp/"+sys.argv[2]+".in","w")
    out.write(str(actual)+"\n")

    while i < numCalls:
        if random.randint(0,100) > 90:
            actual = random.randint(0,tamMax - 1)
            out.write(str(actual)+"\n")
        else:
            actual = (actual + 1) % (tamMax - 1)
            out.write(str(actual)+"\n")
        i += 1

out.close()
