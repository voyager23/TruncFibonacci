/*
 * a_dev.c
 * 
 * Copyright 2023 mike <mike@pop-os>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include <gmp.h>

bool isPanDigit9(mpz_t n)
// Assumes that n is a 9 digit mpz_t
{
    bool flag[10]={false};
    
    mpz_t q,r,d;
    mpz_inits(q,r,d,NULL);
    mpz_set(q,n);
    mpz_set_ui(d,10);
    while (mpz_cmp_ui(q,0) > 0)
    {
        mpz_tdiv_qr(q,r,q,d);   // determine the quotient/remainder mod 10
        if (flag[mpz_get_ui(r)])
        {
            return false;
        } else {
            flag[mpz_get_ui(r)] = true;
        }        
    }
    mpz_clears(q,r,d,NULL);
    
    // test flags
    int i = 1;
    while (i < 10)
        if (flag[i++] == false)
        {
            return false;
        }
    
    return true;
}

int main(int argc, char **argv)
//============================
{
    mpz_t fn,f2,f1;
    
    mpz_inits(fn,f1,f2,NULL);
    
    //mpz_fib_ui(fn,40U);
    
    mpz_set_ui(fn,123456788U);
    
    if (isPanDigit9(fn))
    {
        gmp_printf("%Zd\n",fn);
    } else {
        printf("Not Pandigital\n");
    }
    
    mpz_clears(fn,f1,f2,NULL);
	
	return 0;
}

