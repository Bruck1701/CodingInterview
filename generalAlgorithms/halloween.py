
import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    money = s
    price = p
    gameCounter = 0
    while (money>=0):
      money = money-price
      if money>=0:
        gameCounter+=1
        price = max(m,price-d)
    return gameCounter




result = howManyGames(20,3,6,85)
print(result)

result = howManyGames(20,3,6,80)
print(result)


result = howManyGames(16,2,1,9981)
print(result)