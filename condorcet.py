from scipy.special import comb
from itertools import combinations
import numpy as np


ReLU = lambda x: np.maximum(0, x)
filtered = lambda X: np.array([np.minimum(ReLU(x), 1) for x in X])
complement = lambda whole, part: [x for x in whole if x not in part]


def condorcet(n, p = .65, epsilon = .01):

  p_correct_majority = 0

  # vanilla theorem
  
  if not epsilon:
    for i in range(n//2 + 1, n + 1):
      p_correct_majority += comb(n, i)*p**(i)*(1-p)**(n - i)


  # with Gaussian distribution

  else:
    
    competence_profile = filtered(p + epsilon*np.random.randn(n))
    opposite_competence_profile = 1 - competence_profile

    for i in range(n//2 + 1, n + 1):

      Ci = list(combinations(competence_profile, i))
      Ci_index = list(combinations(range(len(competence_profile)), i))

      for index, combination in enumerate(Ci):

        prod = np.prod(combination)
        complement_index = complement(range(n),Ci_index[index])
        for pm in complement_index:
          prod *= opposite_competence_profile[pm]

        p_correct_majority += prod

  return p_correct_majority
