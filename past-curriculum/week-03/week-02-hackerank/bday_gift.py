#Bday gift
from __future__ import division

n = int(raw_input().strip()) 

array = map(int, raw_input().strip().split(' '))

prob = 1 / 2 #Probability of heads or tails
#print array
#print prob

#expected_value = 1/2 * float(reduce(lambda x,y: x + y,array))
expected_value = float(reduce(lambda x,y: x + y,map(lambda x: x * prob,array)))
print expected_value


