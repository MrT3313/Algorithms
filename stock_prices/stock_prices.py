#!/usr/bin/python

import argparse

# PSEUDO

# function 1
## loop through all elements in the array - 1 (dont want to check the last value with out of bounds)
## set initial low value to array[0]
## set initial high value to None
## set the check array to everying to array[i+1 : ]

### Pass Low, High, & checkArray into function 2

# function 2
## find max value in check array
## -  IF max value in check array > current high value or current high value == None
        ## update high value
## - return high and low values back to function 1

# function 1
## update current high & calculate max profit
## ! LOOP !
### if saved low > array[i] => update saved low if needed
### update check array to array[i + 1 : ]
### Pass Low, High, & checkArray into function 2

# FINAL - calculate and return final profit from saved high and saved low 

## -- *** START CODE *** -- ##

def find_max_profit(prices):
  print(prices)

  saved_LOW = None
  saved_HIGH = None
  saved_TOTAL_profit = None

  for i in enumerate(prices):
    # print(i)
    # print(type(i))

    if saved_LOW == None or (i[0] != len(prices) and i[1] < saved_LOW[1]):
      saved_LOW = i

    if len(prices[i[0] + 1:]) == 0: 
      # 
      break
    else:
      checkArray = prices[i[0] + 1:]
      print('CHECK ARRAY',checkArray)

    result = maxProfit(saved_LOW, saved_HIGH, checkArray)
    print(result)
    saved_LOW = result[0]
    print('LOW RESULT', saved_LOW)

    if result[1] == None:
      saved_HIGH = saved_LOW
      print('HIGH RESULT', saved_HIGH)
    else:
      saved_HIGH = result[1]
      print('HIGH RESULT',saved_HIGH)

    saved_TOTAL_profit = saved_HIGH[1] - saved_LOW[1]
    print('NEW TOTAL PROFIE', saved_TOTAL_profit)

  print('!! ** FINAL RESULT ** !!',[saved_TOTAL_profit, saved_LOW, saved_HIGH])
  return saved_TOTAL_profit

def maxProfit(saved_LOW, saved_HIGH, checkArray ):
  # print(saved_LOW)
  # print(type(saved_LOW))
  # print(saved_HIGH)
  # print(type(saved_HIGH))
  # print(checkArray)

  check_MAX_index = checkArray.index(max(checkArray))
  # print(check_MAX_index)

  print(checkArray[check_MAX_index] )
  print(saved_LOW[1])
  if checkArray[check_MAX_index] > saved_LOW[1]:
    # toReturn_PROFIT = checkArray[check_MAX_index] - saved_LOW[1]
    # print(toReturn_PROFIT)

    # print(saved_HIGH[1])
    print(saved_HIGH)
    print(type(saved_HIGH))
    if saved_HIGH == None or checkArray[check_MAX_index] > saved_HIGH[1]:
      saved_HIGH = (check_MAX_index + saved_LOW[0] + 1, checkArray[check_MAX_index])
      # print(saved_HIGH)

  return [saved_LOW, saved_HIGH]


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([10, 7, 5, 8, 11, 9]))
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))
