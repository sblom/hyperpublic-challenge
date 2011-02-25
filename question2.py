'''
Created on Feb 24, 2011

@author: Scott Blomquist
'''

import sys
from operator import mul

# Constants from problem definition.
KARMA_TOTALS = (2349, # Doug 
                2102, # Jordan
                2001, # Eric
                1747, # Jonathan
                )
ACTIVITY_POINTS = (2,  # Add Place
                   3,  # Add Thing
                   17, # Tag Object
                   23, # Upload Photo
                   42, # Twitter Share
                   98, # Facebook Share
                   ) 

# Determines when we know everything we need to compute final answer.
def are_interesting_activity_counts_known(activity_counts):
    '''Determines when we know everything we need to compute final answer.'''
    for karma_score in KARMA_TOTALS:
        if (not activity_counts.has_key(karma_score)):
            return False
    return True

def main(argv):
    '''Dynamic programming algorithm for computing minimum activities required for each karma score.'''
    max_karma = max(KARMA_TOTALS)
    activity_counts = {}
    new_gen = {0:0} # Base case: Zero score requires Zero activities.
      
    while (not are_interesting_activity_counts_known(activity_counts)):
        # Shift to next generation.
        prev_gen, new_gen = new_gen, {}
        for (karma,min_activities) in prev_gen.items():
            for pointval in ACTIVITY_POINTS:
                if karma + pointval <= max_karma and not activity_counts.has_key(karma+pointval):
                    new_gen[karma+pointval] = min_activities+1
        activity_counts.update(new_gen)
    
    # Answer consists of product of minimum activities required for each staffer's karma total.
    print "Answer:", reduce(mul, [activity_counts[karma] for karma in KARMA_TOTALS])

if __name__ == '__main__':
    main(sys.argv)