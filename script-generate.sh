#!/bin/bash
echo "gerando arquivo de entrada com jmp e loop e ramSize $1 ..."
python3 seqGenerator.py $1 10000 true
python3 seqGenerator.py $1 100000 true
python3 seqGenerator.py $1 500000 true
python3 seqGenerator.py $1 1000000 true
echo "gerando arquivo de entrada com jmp e ramSize $1 ..."
python3 seqGenerator.py $1 10000 false
python3 seqGenerator.py $1 100000 false
python3 seqGenerator.py $1 500000 false
python3 seqGenerator.py $1 1000000 false
