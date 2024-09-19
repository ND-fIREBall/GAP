"""
Copyright (C) 2023 by Kevin Lee

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

----------------------------------------------------------------------

GAP.py

Program to calculate pairing gaps using 2020 AME data using 5 point mass interpolation.
The interpolation method was taken from Mang et al (DOI: https://doi.org/10.1016/0029-5582(65)90564-X).

To run, simply input:

$python3 GAP.py

Language: Python3
University of Notre Dame

Created June 7, 2023 by Kevin Lee
"""

import os
import itertools

pathtodir = os.getcwd()+'/'

isotope = input('please enter isotope: ')

def findZ(elem):
    """
    Returns the atomic number Z of the element
    """
    amedata = open('ame2020.txt','r')
    with amedata as f:
        for line in itertools.islice(f, 35, None):
            break
        Ei = ''
        while Ei != elem:
            line = f.readline()[4:]
            numbers = line.split()
            Ei = numbers[3]
        return int(numbers[1])

def findisotope(Z, A):
    """
    Returns the mass of the isotope
    """
    amedata = open('ame2020.txt','r')
    with amedata as f:
        #skip header lines
        for line in itertools.islice(f, 35, None):
            break
        Ai = 0
        Zi = 0
        while Ai != A or Zi != Z:
            line = f.readline()[4:]
            #if end of fine is reached, return 0 for mass
            if len(line) == 0:
                return 0
            numbers = line.split()
            Ai = int(numbers[2])
            Zi = int(numbers[1])
        
        #get mass of isotope
        masscomponents = line[102:].split()
        for i in masscomponents[1]:
            if i == '#' or i == '.':
                masscomponents[1] = masscomponents[1].replace(i,'')
        
        mass = float('.'.join((masscomponents[0],masscomponents[1])))
        print(Zi,Ai,mass)
    return mass*931.494

#separate element symbol and mass number
elem = ''
strA = ''
A = 0 
for i in isotope:
    if i.isalpha():
        elem = ''.join([elem,i])
    else: 
        strA = ''.join([strA,i])
A = int(strA)
#find atomic number of element
Z = findZ(elem)

#calculate pairing gaps
print('\ncalculating proton gap')
print('Z | A | Mass')
protongap = (1/8) * (findisotope(Z-3,A-3) - 9*findisotope(Z-1,A-1) + 16*findisotope(Z,A) - 9*findisotope(Z+1,A+1) + findisotope(Z+3,A+3))
print('\ncalculating neutron gap')
print('Z | A | Mass')
neutrongap = (1/8) * (findisotope(Z,A-3) - 9*findisotope(Z,A-1) + 16*findisotope(Z,A) - 9*findisotope(Z,A+1) + findisotope(Z,A+3))  

#print final result in keV
print('\nResults for '+isotope)
print('protongap:',abs(protongap)*1000,'keV')
print('neutrongap:',abs(neutrongap)*1000,'keV\n')    
