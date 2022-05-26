'''
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.
'''

def getMoneySpent(keyboards, drives, b):
    all_possible_costs = []
    for k in keyboards:
        for j in drives:
            cost = k+j
            if cost <= b:
                all_possible_costs.append(cost)
    if len(all_possible_costs)>0:
            return max(all_possible_costs)
    return -1

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

spent = getMoneySpent(keyboards,drives,b)
print(spent)

