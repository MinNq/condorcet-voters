"""
Condorcet's voters:

We analyse the behaviour of majority decisions by
estimating the probability of such decisions being
correct on a range of population sizes.

Assumptions:

- There are only 2 options being voted for, of which 
one is correct.
- Each voter in our pool has a correct probability of 
a normal distribution with mean = p and variance = epsilon.
- The probability of a population's majority being correct is estimated 
with 3000 runs on that population.
"""

import numpy as np
import matplotlib.pyplot as plt


def condorcet(pool, p = .65, epsilon = .05, run = 3000):

  correct_majority_count = 0

  for sample_count in range(run):

    votes = np.random.rand(pool)
    thresholds = p + epsilon*np.random.randn(pool)
      
    correct_voters = [vote for number, vote in enumerate(votes) if 
                        vote < thresholds[number]] 

    correct_majority_count += 1 if 2*len(correct_voters) > pool else 0

    p_correct_majority = correct_majority_count/float(run)

  return p_correct_majority

majority_correctness = []

for pool in range(100):
  majority_correctness.append(condorcet(pool))

plt.figure(figsize = (16,9))

plt.plot(range(100), majority_correctness)
plt.title('p = .65, epsilon = .05')
plt.ylabel('Probability that majority vote is correct')
plt.xlabel('Number of voters')

plt.show()
