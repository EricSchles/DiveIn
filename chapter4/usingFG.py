#makes use of the functionGen.py module to generate multiple
#functions of a given type.

import functionGen

def output(data, format="add"):
    output_function = getattr(functionGen, "output_%s" % format)
    return output_function(data)

if __name__ == "__main__":
    print output(5) #produces a number
    print output(6,"string") #produces a string
