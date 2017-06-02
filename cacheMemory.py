
import sys
import random
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

def associativeMap(sequence, cache, way, ramSize):
    cacheMiss = 0
    cacheHit = 0
    #victim = [0] * way
    #vic = 0
    cacheMapValue = int(len(cache)/way)
    ramMapValue = ramSize/way
    setValue = 0

    #print("\nCM "+str(cacheMapValue)+"\nRM: "+str(ramMapValue))

    for current in sequence:
        #print(cache)
        setValue = int(current/ramMapValue)
        if current in cache[setValue * cacheMapValue : (setValue+1) * cacheMapValue]:
            cacheHit += 1
        else:
            cacheMiss += 1
            #cache[victim[setValue] + (setValue * cacheMapValue)] = current
            cache[random.randint(setValue * cacheMapValue, ((setValue+1) * cacheMapValue)-1)] = current
            #victim[setValue] = (victim[setValue] + 1) % cacheMapValue
        #print(str(current))
        #print(cache)
        #input()

    print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))

#################################

if __name__ == "__main__":
    text = open(sys.argv[3],"r")
    sequence = []

    for line in text.readlines():
        sequence.append(int(line.replace("\n","")))

    text.close()

    print("File: "+ sys.argv[3])
    cache = [None] * int(sys.argv[1])
    ramSize = 2048

    print("Direct ")
    directMap(sequence,cache,ramSize)

    cache = [None] * int(sys.argv[1])
    way = int(sys.argv[2])

    print("\nAssociative: ")
    associativeMap(sequence, cache, way ,ramSize)
