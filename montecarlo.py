import numpy as np

def uniform(n, m):
    '''Function for uniform outcome. This function return a number between 1 to n with equal probability'''
    return np.random.randint(1, n+1, size = m)

print(uniform(1, 1))
print(uniform(1, 10))
print(uniform(1,100))

print(uniform(6, 1)) #This outcome depicts the dice throwing event
print(uniform(6, 10))
print(uniform(6,100))

'''Monte Carlo - Estimating probability by simulation.
We define 1 as heads and 2 as tails for our computation'''
no_heads = 0   #variable for storing number of heads
for i in range(10000): #repeat 1000000 times
    if uniform(2, 1) == 1: #check if coin toss is heads
        no_heads = no_heads + 1
print(no_heads/10000) #probability estimate by Monte Carlo


no = 0   #variable for storing number of event occurence
for i in range(10000): #repetitions
    die = uniform(6,1)  #experiment
    if die == 1 or die == 3 or die == 5: #Event: odd number is seen after a toss
        no = no + 1
print(no/10000) #probability estimate by Monte Carlo