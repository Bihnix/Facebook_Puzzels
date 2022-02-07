from typing import List
# Write any import statements here
import numpy as np
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  A = R *  C
  p_value = (np.sum(G)/A)
  return p_value
