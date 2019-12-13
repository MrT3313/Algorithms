#!/usr/bin/python

import sys

def recurse(prev, n, all_results):
  #Base Case
  if n == 0:
    all_results.append(prev)
    return
  
  #Recursive Step
  recurse(prev + ['R'], n-1, all_results)
  recurse(prev + ['P'], n-1, all_results)
  recurse(prev + ['S'], n-1, all_results)

def rock_paper_scissors(n):

  results = []
  recurse([], n, results)

  print(results)
  return results


# rock_paper_scissors(2)
rock_paper_scissors(3)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')