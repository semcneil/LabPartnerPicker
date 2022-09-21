#!/usr/bin/env python3
#
# listLabGroups.py
#
# Lists the possibilities of lab partners based on file containing
# one name per line.
#
# Author: Seth McNeill
# Date:   2022 August 24

import datetime     # for date/time functions
import pdb          # for debugging
import argparse     # This gives better command line argument functionality
from itertools import combinations  # creates combinations based on list and n
from numpy import random  # for permutations


def evenGroups(nameList):
    '''Creates pairs of names that don't overlap and 
       are only used once for a name list with an even
       number of names'''
    nNames = len(nameList)
    if nNames % 2: # odd number of names
        print("Error: Odd number of names")
        #return(-1)
    allGroups = []
    nHalf = int(nNames/2)
    for jj in range(nHalf):
        nameList = nameList[jj:] + nameList[:jj]
        firstHalf = nameList[:nHalf]
        lastHalf = nameList[nHalf:]
        print(f'{firstHalf}\n{lastHalf}')
        for ii in range(nHalf):
            rotList = lastHalf[ii:] + lastHalf[:ii]
            groups = tuple(zip(firstHalf,rotList))
            usedCombinations = [set(group) for labGroups in allGroups for group in labGroups]
            print(any(set(group) in usedCombinations for group in groups),end='')
            print(f': {groups}')
            #pdb.set_trace()
            if not any(set(group) in usedCombinations for group in groups):
                allGroups.append(groups)
    return(allGroups)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-f','--namefile',
                        help='Name of file containing one name per line')

    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    with open(args.namefile, 'r') as f:
        nameList = f.readlines()
    
    nameList = [n.strip() for n in nameList]
    nNames = len(nameList)
    print(f'#names: {nNames}')
    randNames = random.permutation(nameList)
    print(randNames)

    randNames = nameList
    
    # https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/
    if nNames % 2:  # odd number of names
        print("Odd number of names")
        # check whether user wants groups of 1 or 3
        allGroups = evenGroups(randNames)
        ii = 0
        for groups in allGroups:
            usedNames = set([name for group in groups for name in group])
            unused = set(randNames).difference(usedNames).pop()
            groups.append(unused)
            print(f'Lab {ii}: {groups}')
            ii += 1        
    else:
        print("Even number of names")
        groups = evenGroups(randNames)
        ii = 0
        for group in groups:
            print(f'Lab {ii}: {group}')
            ii += 1


    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')