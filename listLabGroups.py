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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--namefile',
                        help='Name of file containing one name per line')

    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    with open(args.namefile, 'r') as f:
        nameList = f.readlines()
    
    nameList = [n.strip() for n in nameList]
    nameCombsIter = combinations(nameList, 2)  # get the combinations 
    nameCombs = [namePair for namePair in nameCombsIter]  # convert to list for operating on
    for nameComb in nameCombs:
        print(nameComb)
    
    # try to build lab partners for each class
    # https://flexiple.com/python/check-if-list-is-empty-python/
    labList = []
    usedNames = []
    labNum = 1  # lab count number
    while nameCombs[:]:  # while nameCombs isn't empty
        # start the lab list with the first element still in the list
        if not labList:  # labList is empty
            usedNames.extend(nameCombs[0])
            labList.append(nameCombs.pop(0))
        # Add tuples that don't contain the names already in the list
        for names in nameCombs:
            # check to see if any names in names are in usedNames
            # if not, add names to labList and remove from nameCombs
            if not any(n in usedNames for n in names):
                usedNames.extend(names)
                labList.append(names)
                nameCombs.remove(names)
        print(f'Lab {labNum}:\n {labList}')
        labNum += labNum
        labList = []
        usedNames = []
    pdb.set_trace()

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')