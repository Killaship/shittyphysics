
g = 6.673 * (10**-11) # Gravitational constant
results = []
masses = [[]]
positions = [[]]
iterations = 1
bodies = {"body1": {"mass": 100, "pos": [1, 0]}, "body2": {"mass": 100, "pos": [6, 0]},   }

"""

The following function is an absurdly shitty way to find distance in Python.
It takes 2 arrays, each with 2 numbers, as a pair of coordinate pairs.
Then, it uses the Manhattan Distance method to calculate how far apart the two points are.
Stack Overflow kinda sucks.

"""
def minimum_distance(p1, p2): 

    i1, i2 = int(p1[0]), int(p2[0])

    # if both x-coordinates are floats and they have the same integer part
    if i1 != p1[0] and i2 != p2[0] and i1 == i2:

        # find the decimal parts
        d1, d2 = p1[0] - i1, p2[0] - i2

        # find the smaller "C"
        x = min(d1 + d2, (1-d1) + (1-d2))

        # add the y distance to the "C" distance
        return abs(p1[1] - p2[1]) + x

    # repeat with the "y-coordinates are floats" case
    i1, i2 = int(p1[1]), int(p2[1])
    if i1 != p1[1] and i2 != p2[1] and i1 == i2:
        d1, d2 = p1[1] - i1, p2[1] - i2
        y = min(d1 + d2, (1-d1) + (1-d2))
        return abs(p1[0] - p2[0]) + y

    # simple case, return the Manhattan distance
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])



def calcforce(mass1, mass2, distance):
    F = (g * mass1 * mass2) / distance ** 2
    print("Force =", F)
    return F # Fg = (G*M1*M2)/D^2

def iterate():
    while 1:
        i = 0
        for key, value in bodies.items():
            print(value)
           # positions[iterations][i] = body["pos"]
           # print(body["mass"])
           # masses[iterations][i] = body["mass"]
            
            i += 1
       # calcforce(masses[iterations][0], masses[iterations][1], minimum_distance(positions[iterations][0], positions[iterations][1]))
        iterations += 1
   
    
iterate()
    
#        if(results[iterations - 1] == results[iterations]): # If the current results are the same as the last, end.
#            print()
#            break
