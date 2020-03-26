from __future__ import division

import iotbx.pdb
#import iotbx.xplor.map
import libtbx as libtbx
from cctbx.miller import fft_map
from libtbx.math_utils import ifloor, iceil
import libtbx.option_parser
import sys

def pdbMap(fileName):
  d_min = 0.4
  pdb_inp = iotbx.pdb.input(fileName)
  xray_structure = pdb_inp.xray_structure_simple()
  print("d_min:", d_min)
  f_calc = xray_structure.structure_factors(d_min=d_min).f_calc()
  x= f_calc.amplitudes()
  file2 = open(r"computedValues.txt", 'w')
  for i in x:
    for m in i:
      file2.write(str(m) + " ")
    file2.write('\n')
  fft_map = f_calc.fft_map()
  n = fft_map.n_real()
  print("unit cell gridding:", n)
  fft_map.as_xplor_map(file_name="unit_cell.map")
  block_first = tuple([ifloor(i*0.2) for i in n])
  block_last = tuple([max(f+10, iceil(i*0.7)) for f,i in zip(block_first, n)])
  print("block first:", block_first)
  print "block last: ", block_last
  fft_map.as_xplor_map(file_name="block.map", gridding_first=block_first, gridding_last=block_last)


pdbMap("6f0o.pdb")