#!/usr/bin/python3
import random
random_coin_side = random.randint(1, 2)
print("Heads") if random_coin_side == 1 else print("Tails")
