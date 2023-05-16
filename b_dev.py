#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  b_dev.py
#  
#  Copyright 2023 mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

# ~ import time

# ~ def fib(n):
    # ~ v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    # ~ for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        # ~ calc = v2*v2
        # ~ v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        # ~ if rec=='1':
            # ~ v1, v2, v3 = v1+v2, v1, v2
    # ~ return str(v2)[:9]
    
# ~ def compute(number):
    
    # ~ f1 = 1
    # ~ f2 = 1
    # ~ count = 2
    # ~ while True:
        # ~ count += 1
        # ~ fn = (f2 + f1) % 10**9
        # ~ if count == number:
          # ~ return ("\nLast 9 digits are " + str(fn) +  "\n\nFirst 9 digits are " + fib(count))
          # ~ break
        # ~ f1 = (f2 % 10**9)
        # ~ f2 = fn
        
# ~ if __name__ == "__main__":
    # ~ while True:
      # ~ userinput = input("Please input an integer: ")
      # ~ start_time = time.time()
      # ~ temp = compute(int(userinput))
      # ~ print(temp)
      # ~ break
    # ~ print("--- %s seconds ---" % (time.time() - start_time))
    
    
    
def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2

def main(args):
    Fib = {}
    fin = open('Fib2000.txt','r')
    l = fin.readline()
    while l != "":
        print(l)
        m = l.split()
        Fib[m[0]] = m[1]
        l = fin.readline()
    for f in Fib.items():
        print(f)
        
    print(fibonnaci(40))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
