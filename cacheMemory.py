
import sys
def directMap(sequence,cache,ramSize):
    cacheMiss = 0
    cacheHit = 0
    mapValue = ramSize/len(cache)

    for current in sequence:
        #print (cache)

        if (cache[int(current/mapValue)] != current) or (cache[int(current/mapValue)] == None):
            cacheMiss += 1
            cache[int(current/mapValue)] = current
        else:
            cacheHit += 1

        # print (current)
        # print (cache)
        # print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))
        # input()

    print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))

def associativeMap(sequence, cache, ramSize):
    cacheMiss = 0
    cacheHit = 0
    victim = 0

    for current in sequence:
        if current in cache:
            cacheHit += 1
        else:
            cacheMiss += 1
            cache[victim] = current
            victim = (victim + 1) % len(cache)

    print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))
#################################

if __name__ == "__main__":
    text = open(sys.argv[2],"r")
    sequence = []

    for line in text.readlines():
        sequence.append(int(line.replace("\n","")))

    text.close()

    print("File: "+ sys.argv[2])
    cache = [None] * int(sys.argv[1])
    ramSize = 1000

    print("Direct ")
    directMap(sequence,cache,ramSize)

    cache = [None] * int(sys.argv[1])

    print("\nAssociative: ")
    associativeMap(sequence, cache, ramSize)
