# -*- coding: utf-8 -*-
import time
import sys

def append_color(msg, color='default'):
    return '{}{}{}'.format(COLOR[color], msg, COLOR['default'])

COLOR = {
    'default' : '\033[m',
    'green'   : '\033[1;32m',
    'red'     : '\033[1;31m',
    'yellow'  : '\033[1;33m',
    'cyan'    : '\033[1;36m'
}

continents = [
    ('Africa',0.017),
    ('Antarctica',0.006),
    ('Asia',0.026),
    ('Australia',0.008),
    ('Europe',0.017),
    ('North America',0.015),
    ('South America',0.012)
]

print 'Searching for the most handsome guy in the world:'

for continent in continents:
    for i in xrange(101):
        time.sleep(continent[1])
        sys.stdout.write("\r{color:>14s} {subject:.<20s}[{oct:<10}]".format(
            color   = append_color(str(i)+'%', 'cyan'),
            subject = continent[0],
            oct     = '#'*(i/10)
            )
        )
        sys.stdout.flush()
    print

print 'Analyzing data...'
time.sleep(10)

print '== Result =='
print 'Subjects: 6,731,528,121'
print 'Matched: 1'
print '\tSubject Name: C**** C***, Taiwan'
print '== End of Result =='

