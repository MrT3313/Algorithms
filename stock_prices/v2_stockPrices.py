# ALLOW FOR NEGATIVE RETURN

def find_max_profit(prices):
    print('__MAIN__: INITIAL PRICES ARRAY',prices)

    low_value = None
    high_value = None
    max_PROFIT = None

    for i in enumerate(prices):
        # print(i)
        # print(len(prices))
        # print(i[0])

        if low_value is None or (i[0] != len(prices) - 1 and i[1] < low_value[1]):
            low_value = i
            print('** updated ** low value',low_value) 

            # Get Check Array
            checkArray = prices[low_value[0] + 1: ]
            # print(low_value, checkArray)

            # Find max profit for THIS minimum
            curr_maxProfit = calculate_maxProfit(i, low_value, checkArray)
            print('__MAIN__: result FROM __HELPER__',curr_maxProfit)
            # print(curr_maxProfit[0])
            # print(max_PROFIT)

            if max_PROFIT is None or curr_maxProfit[0] > max_PROFIT:
                high_value = curr_maxProfit[2]
                print('** updated ** high value', high_value)
                max_PROFIT = curr_maxProfit[0]
                print('** updated ** max profit', max_PROFIT)
        else:
            continue

    print('!! *** FINAL RESULT *** !!',max_PROFIT, low_value, high_value)
    return (max_PROFIT)

def calculate_maxProfit(i, low_value, checkArray):
    # print(i)
    # print(low_value)
    # print(checkArray)

    currentHigh = (checkArray.index(max(checkArray)) + i[0] + 1, checkArray[checkArray.index(max(checkArray))])
    print('__HELPER__: current HIGH ', currentHigh)
    print('__HELPER__: current LOW ', low_value)

    maxProfit = currentHigh[1] - low_value[1]
    print('__HELPER__: MAX PROFIT ',maxProfit)

    # print( maxProfit, low_value, currentHigh )
    return ( maxProfit, low_value, currentHigh )



print(find_max_profit([50, 10, 30, 90, 3, 4, 5]))

# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([10, 7, 5, 8, 11, 9]))
# print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))