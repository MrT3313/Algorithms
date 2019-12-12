#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # - Data Check - 
  # print(recipe)
  # print(ingredients)

  # - Variables -
  minMax = None


  for i in recipe.items():
    # print(i)
    # print(i[1])

    try:
      check = ingredients[i[0]] / i[1]
    except KeyError as e:
      print('KeyError', 0)
      return 0

    if check < 0:
      result = 0
    else:
      result = math.floor(check)

    print(minMax)
    print(i[0],result)

    if minMax == None:
      minMax = result

    if minMax > result:
      minMax = result
    
  print('RESULT',minMax)
  return minMax
  

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

