#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  d_dev.py
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
#  329468 finds soln in 52 seconds

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2  
    return v2
    
def isPandigital1_9(n):
    
    # reduce n to 9 leftmost digits
    n = int(str(n)[:9])
    
    # Return True if 9 digit number n contains digits 1 to 9
    s = set()
    count = 0
    while n:
        count += 1
        if count > 9:
            return False
        d = n % 10
        n = n // 10
        if d in s or d == 0:
            return False
        else:
            s.add(d)
    return True
    

# NO CORRECT SOLUTION FOUND

def main(args):
    F1 = 39088169   
    F2 = 63245986   # 9 LSD of Fibonacci number
    
    h1 = 39088169
    h2 = 63245986   # 12 MSD of Fibonacci number
    
    count = 39
    
    while True:
        Fn = (F1 + F2) % 10**9
        F1 = F2
        F2 = Fn
        
        hn = (h1 + h2) 
        # using 6 more significant digits
        while hn > 10**(9+9):
            hn //= 10

        h1 = h2
        h2 = hn
        
        count += 1
        if count%1000 == 0:
            print(count, end=" ")
        
        if isPandigital1_9(Fn) and isPandigital1_9(hn):
            print()
            print(f"Solution found at {count}")
            break
        
    return 0
        

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
