#!/bin/bash
echo "gerando resultados com loop e jmp..."
bash generate-results.sh loop $1 $2 > assets/loop.txt
echo "gerando resultados com jmp..."
bash generate-results.sh jmp $1 $2 > assets/jmp.txt
echo "gerando graph loop..."
python plot.py assets/loop.txt loop $1 $2
echo "gerando graph jmp..."
python plot.py assets/jmp.txt jmp $1 $2
