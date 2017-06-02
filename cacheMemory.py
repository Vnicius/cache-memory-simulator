
import sys
import random
def directMap(sequence,cache,ramSize):
    cacheMiss = 0
    cacheHit = 0
    mapValue = ramSize/len(cache)

    for current in sequence:
        #print (cache)

        #if (cache[int(current/mapValue)] != current):
        if (cache[current % len(cache)] != current):
            cacheMiss += 1
            #cache[int(current/mapValue)] = current
            cache[current % len(cache)] = current
        else:
            cacheHit += 1

        # print (current)
        # print (cache)
        # print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))
        # input()

    # print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))
    # print("CH: "+str((cacheHit/len(sequence))*100)[:5]+"%")
    return str(cacheHit)

def associativeMap(sequence, cache, way, ramSize):
    cacheMiss = 0
    cacheHit = 0
    victim = [0] * way
    #victim = 0
    cacheMapValue = int(len(cache)/way)
    ramMapValue = ramSize/way
    setValue = 0

    #print("\nCM "+str(cacheMapValue)+"\nRM: "+str(ramMapValue))


    ### Direct Associative ###
    # for current in sequence:
    #     if current in cache:
    #         cacheHit += 1
    #     else:
    #         cacheMiss += 1
    #         cache[victim] = current
    #         victim = (victim + 1) % len(cache)

    for current in sequence:
        #print(current)
        setValue = int(current/ramMapValue)
        #print(setValue)
        if current in cache[setValue * cacheMapValue : (setValue+1) * cacheMapValue]:
            #print("POS: "+str(setValue * cacheMapValue)+" : "+str((setValue+1) * cacheMapValue))
            cacheHit += 1
        else:
            cacheMiss += 1
            #print(victim[setValue])
            cache[victim[setValue] + (setValue * cacheMapValue)] = current
            #cache[random.randint(setValue * cacheMapValue, ((setValue+1) * cacheMapValue)-1)] = current
            victim[setValue] = (victim[setValue] + 1) % cacheMapValue
        #print(str(current))
        #print(cache)
        #input()

    #print("CH: "+str(cacheHit)+"\nCM: "+str(cacheMiss))
    #print("CH: "+str((cacheHit/len(sequence))*100)[:4]+"%")
    return str(cacheHit)

#################################

# python3 cacheMemory.py file.in tamRam tamCache way

if __name__ == "__main__":
    text = open(sys.argv[1],"r")
    sequence = []

    for line in text.readlines():
        sequence.append(int(line.replace("\n","")))

    text.close()

    #print("File: "+ sys.argv[4])
    cache = [None] * int(sys.argv[3])
    ramSize = int(sys.argv[2])

    try:
        way = int(sys.argv[4])
        #print("\nAssociative: ")
        print(str(len(sequence))+" "+associativeMap(sequence, cache, way ,ramSize))
    except Exception as e:
        #print("Direct: ")
        print(str(len(sequence))+" "+directMap(sequence,cache,ramSize))
