#!/bin/bash
python3 cacheMemory.py "assets/$1/10000.in" $2 $3
python3 cacheMemory.py "assets/$1/100000.in" $2 $3
python3 cacheMemory.py "assets/$1/1000000.in" $2 $3
python3 cacheMemory.py "assets/$1/10000.in" $2 $3 1
python3 cacheMemory.py "assets/$1/100000.in" $2 $3 1
python3 cacheMemory.py "assets/$1/1000000.in" $2 $3 1
python3 cacheMemory.py "assets/$1/10000.in" $2 $3 2
python3 cacheMemory.py "assets/$1/100000.in" $2 $3 2
python3 cacheMemory.py "assets/$1/1000000.in" $2 $3 2
python3 cacheMemory.py "assets/$1/10000.in" $2 $3 4
python3 cacheMemory.py "assets/$1/100000.in" $2 $3 4
python3 cacheMemory.py "assets/$1/1000000.in" $2 $3 4
