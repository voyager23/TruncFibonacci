#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  a_dev.py
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


def main(args):
    # standard Fibonacci series to 2 * 10^15
    Fib = [39088169,63245986]
    Trunc_Fib = [390881,632459]
    a = 0
    b = 1
    while True:
        Fib.append(Fib[a]+Fib[b])
        Trunc_Fib.append((Trunc_Fib[a]+Trunc_Fib[b]))
        a += 1
        b += 1
        while Trunc_Fib[b] > 10000000:
            Trunc_Fib[b] //= 10  
        print(Fib[b], Trunc_Fib[b])
        if Fib[b] > 2*pow(10,15):
            break
            
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
