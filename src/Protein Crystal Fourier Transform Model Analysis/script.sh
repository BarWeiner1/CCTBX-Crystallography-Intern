#!/bin/bash
#cd ~/Applications/phenix-1.16-3549
#source /Applications/phenix-1.16-3549/phenix_env.sh

for ((i=1;i<1000;i++)); do
ranNum2=$[RANDOM%300+9700]
phenix.dynamics /Users/barweiner/PycharmProjects/cctb/6f0o.pdb temperature=500 steps=$ranNum2 output_file_name_prefix=$i$_shaken write_geo_file=False
#mv 6f0o.pdb 6f0o$i$_shaken.pdb
#Python3 /Users/barweiner/PycharmProjects/cctb/AllOperations.py 6f0o$i.pdb
done
