#!/bin/bash
cd ~/Desktop/Scwrl/
for ((i=96;i<578;i++)); do
./Scwrl4 -i R$i.pdb -o A$i.pdb
done
