g = 6.673 * (10**-11) # Gravitational constant

bodies = {"body1": {"mass": 100, "pos": [1, 0]},   }

def calcforce(mass1, mass2, distance):
    return (g * mass1 * mass2) / distance ** 2 # Fg = (G*M1*M2)/D^2

def iterate():
