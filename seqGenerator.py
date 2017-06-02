import random
import sys

tamMax = int(sys.argv[1])
i = 1
numCalls = int(sys.argv[2])
out = open("assets/"+sys.argv[2]+".in","w")
actual = 0
out.write(str(actual)+"\n")

while i < numCalls:
    if random.randint(0,100) > 90:
        actual = random.randint(0,tamMax - 1)
        out.write(str(actual)+"\n")
    else:
        actual = (actual + 1) % (tamMax - 1)
        out.write(str(actual)+"\n")
    i += 1

# loops
# loop = [0]
# maxLoop = 100
# while i < numCalls:
#     rNum = random.randint(0,100)
#     #loop
#     if rNum > 99:
#         loopCount = random.randint(1, len(loop))
#         if loopCount > maxLoop:
#             loopCount = maxLoop
#         for v in loop[len(loop)-loopCount-1:]:
#             loop.append(v)
#         actual = loop[-1]
#         i += (loopCount + 1) % (tamMax - 1)
#     #jump
#     elif rNum > 80:
#         actual = random.randint(0,tamMax - 1)
#         loop.append(actual)
#     else:
#         actual = (actual + 1) % (tamMax - 1)
#         loop.append(actual)
#     i += 1
#
# for value in loop:
#     out.write(str(value)+"\n")

out.close()
