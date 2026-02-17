# 8. Random 4 digit generator
from random import randint

RAND_NUM_str = ""
RAND_NUM=0

# Loop to make a string of random 0s and 1s
for i in range(4):
    a=str(randint(0,1))
    RAND_NUM_str = RAND_NUM_str+a

# Converts binary integer to decimal
DECIMAL_NUM = int(RAND_NUM_str, 2)

print("Random 4 digit binary number: ", RAND_NUM_str)
print("Decimal value: ", DECIMAL_NUM)

