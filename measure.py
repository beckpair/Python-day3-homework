# Measuring square footage of a house

def sq_foot():
    lth = input("What is the length of your house? ")
    wid = input("What is the width of your house? ")
    length = int(lth)
    width = int(wid)
    squarefeet = length * width
    return (squarefeet)

# Measuring circumference

def circ():
    from math import pi
    d = input("What is the diameter of your umbrella?" )
    diameter = int(d)
    circumference = pi * diameter
    return (circumference)
    
