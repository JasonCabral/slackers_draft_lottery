#!/usr/bin/env python
# coding: utf-8

import sys
import string
from numpy.random import choice
from time import time
import random
import numpy as np
import pandas as pd

# run on command line
input_file = sys.argv[1]
skip_animation = sys.argv[2] == '--no_anim' if len(sys.argv) > 2 else False

# run in notebook
# input_file = 'standings.csv'

with open(input_file, 'r') as f:
    teams = [line.strip() for line in f]
    teams.reverse()

standings = pd.read_csv(input_file)

# Check Probability
    
# list = []
# N = float(np.sum(standings.balls))
# for i in range(1,100000):
#     list.append(choice(standings.team, 1, p=[row['balls'] / N for index, row in standings.iterrows()])[0])

# d = {'team': [row['team'] for index, row in standings.iterrows()], 'prob': [row['balls'] / N for index, row in standings.iterrows()]}
# prob_df = pd.DataFrame(data=d)
# prob_df
# for i in set(list):
#     print(i, list.count(i)/100000)

# Run the drawing, removing selected teams once chosen
iter_standings = standings.copy()
order = []
pick = 1
while len(iter_standings)>0:
    N = float(np.sum(iter_standings.balls))
    draw = choice(iter_standings.team, 1, p=[row['balls'] / N for index, row in iter_standings.iterrows()])[0]
    order.append(draw)
    delete_row = iter_standings[iter_standings["team"] == draw].index
    iter_standings.drop(delete_row, axis=0, inplace=True)
    pick += 1

# Print some gibberish to make it look like the program is thinking really hard
def print_gibberish(time_to_run, str_len=50):
    start = time()
    while True:
        sys.stdout.write('\r')
        if time()-start > time_to_run:
            sys.stdout.write(' '*str_len)
            return
        else:
            sys.stdout.write(''.join(random.choice(string.ascii_letters) for x in range(str_len)))

# Print Balls
print('')
print("Starting Balls")
print(standings.sort_values('balls').to_string(index=False))

# Output the final draft results
gibberish_time = 1.5
print('')
for i, result in enumerate(reversed(order)):
    if not skip_animation:
        print_gibberish(gibberish_time)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print('#%d:\t%s' % (len(order)-i, result))
    gibberish_time += 0.3 # get more dramatic with each result






