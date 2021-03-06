#!/usr/bin/env python3

#######################################
# Generates some arrays of constants for
# shell related stuff
#######################################

import argparse
import sys
from mpmath import mp # arbitrary-precision math

# Note that types are being stored as a string. This is so mpmath
# can parse it without turning it into a (possibly) lesser-precision float 
parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, required=True,               help="Output file name base (no extension)")
parser.add_argument("--max-am",    type=int, required=True,               help="Maximum angular momentum value to go to")
parser.add_argument("--dps",      type=int, required=False, default=256, help="Decimal precision/sig figs to use/calculate")
args = parser.parse_args()

# Set the dps option
mp.dps = args.dps

# Convert stuff to mpmath
maxam = args.max_am

print("------------------------------------")
print("Options for gen_shellconstants:")
print("   Max am: {}".format(maxam))
print("      DPS: {}".format(args.dps))
print("------------------------------------")


# For normalization
# c = pi**(3/2) * (2L-1)!! / 2**L 

normfac = [None] * (maxam+1)

normfac[0] = mp.power(mp.pi, 1.5)
normfac[1] = normfac[0] / mp.mpf(2.0)

for l in range(2, maxam+1):
  normfac[l] = normfac[l-1] * mp.mpf(2*l-1) / mp.mpf(2.0)
  

# Output to file
with open(args.filename + ".c", 'w') as f:
  f.write("/*\n")
  f.write(" Generated with:\n")
  f.write("   " + " ".join(sys.argv[:]))
  f.write("\n")
  f.write("------------------------------------\n")
  f.write("Options for gen_shellconstants:\n")
  f.write("   Max am: {}\n".format(maxam))
  f.write("      DPS: {}\n".format(args.dps))
  f.write("------------------------------------\n")
  f.write("*/\n\n")

  
  f.write("/* A prefactor for normalization. c = pi**(3/2) * (2l-1)!! / 2**l\n")
  f.write("   where l is the angular momentum\n")
  f.write("*/\n")
  f.write("const double norm_fac[{}] = \n".format(maxam+1))
  f.write("{\n")

  for i,n in enumerate(normfac):
      f.write("/* l = {:4} */  {:32},\n".format(i, mp.nstr(n, 18)))
  f.write("};\n")

with open(args.filename + ".h", 'w') as f: 
  f.write("#pragma once\n")
  f.write("\n")
  f.write("/*! The maximum value of L for which we have precomputed a\n")
  f.write("*  part of the normalization\n")
  f.write("*/\n")
  f.write("#define SHELL_PRIM_NORMFAC_MAXL {}\n".format(maxam))
  f.write("\n")
