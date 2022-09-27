#!/usr/bin/env python3
#
# create_student_list.py
#
# Lists the possibilities of lab partners based on file containing
# one name per line. Utilizes the Round Robin scheduling algorithm
# to accomplish this.
#
# Author: Nick Axmaker
# Date:   2022 September 21

import datetime     # for date/time functions
import argparse     # This gives better command line argument functionality
from numpy import random  # for permutations
import pdb

def round_robin(name_list):
    count = len(name_list)
    even = 1 - (count & 1)
    poly = name_list[even:]
    for _ in range(count - even):
        pairs  = [(name_list[0], poly[0])] * even
        pairs += [(poly[i], poly[count - i - even]) for i in range(1, (count + 1) // 2)]
        yield(pairs)
        poly = poly[1:] + poly[:1]

def main(args):
    """
    Here's what I'd do if I were you: 
    
    Let this create pairings for each lab day of the year. On each day, there is one 
    student who is a "sitout" for that day. Each student gets it once (assuming we're not
    using the numlabs limiter). For the sitout each day, let them decide which group they
    want to be a part of. This would be a fun "special" day for that student and would 
    allow them to work with who they want once per set of labs.

    It's not completely efficient when it comes to pairing groups of 3, of course, but
    adds the element of "fun" that students would appreciate in a class as each gets that
    special day of choosing who they work with. Choice is a good thing sometimes, I think?

    Alternatively, since no group of college students all shows up to lab, you could use the "sitout" 
    student to fill groups where a student is missing that day, since I know you don't like fun. 
    """
    with open(args.namefile, 'r') as f:
        name_list = f.readlines()
    
    name_list = [n.strip() for n in name_list]
    name_list = random.permutation(name_list).tolist()

    if not args.numlabs:
        for day, pairs in enumerate(round_robin(name_list), 1):
            sitout = set(name_list).difference(*pairs)
            print(f'Lab {day}:')
            for pair in pairs:
                print(f'{pair[0]} - {pair[1]}')
            if(len(sitout) > 0):
                print(f'Fill-in: {sitout.pop()}')
            print('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--namefile',
                        help='Name of file containing one name per line',
                        required=True)
    parser.add_argument('-','--numlabs',
                        help='Number of labs')

    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    main(args)

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')

