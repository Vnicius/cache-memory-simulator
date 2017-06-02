import random
import sys

tamMax = 20
i = 1
numCalls = int(sys.argv[1])
out = open(sys.argv[1]+".in","w")
actual = 0
out.write(str(actual)+"\n")

while i < numCalls:
    if random.randint(0,100) > 80:
        actual = random.randint(0,tamMax - 1)
        out.write(str(actual)+"\n")
    else:
        actual = (actual + 1) % (tamMax - 1)
        out.write(str(actual)+"\n")
    i += 1

out.close()
