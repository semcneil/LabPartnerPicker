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
    nameCombs = combinations(nameList, 2)
    for nameComb in nameCombs:
        print(nameComb)
    pdb.set_trace()

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')