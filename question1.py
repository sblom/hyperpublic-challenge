'''
Created on Feb 24, 2011

@author: Scott Blomquist
'''

from operator import add
import sys

def influence(recruit_matrix, uid):
    '''Recursively compute the influence of a given user. Assumes: cycles CANNOT occur in recruit graph.'''
    invitees = reduce(add, map(lambda(ch): 1 if ch == 'X' else 0, recruit_matrix[uid]), 0)
    
    if invitees == 0:
        # Obviously not (yet?) a card-carrying product evangelist...
        return 0
    else:
        # Influence score is # of user's invitees plus sum of his invitees' influence scores. 
        return invitees + reduce(add, map(lambda(a,b):influence(recruit_matrix, a), filter(lambda(a,b): True if b == 'X' else False, enumerate(recruit_matrix[uid]))), 0)

def main(argv):
    if len(argv) < 2:
        print "Usage:\n\tquestion1.py <recruitmatrix.txt>"
        sys.exit(1)
    
    # Read in recruit matrix.
    with open(argv[1]) as recruitfile:
        recruit_matrix = [[ch for ch in line.strip()] for line in recruitfile.readlines()]
    
    # Compute all influence scores.
    influences = [influence(recruit_matrix, id) for id in xrange(len(recruit_matrix))]

    # Answer for challenge consists of 3 highest influence scores concatenated.
    influences.sort(reverse=True)
    print "Answer:", str(influences[0]) + str(influences[1]) + str(influences[2])

if __name__ == '__main__':
    main(sys.argv)
