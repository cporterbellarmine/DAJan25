print ("Welcome to the affine cypher!\n")

encryption = input("Would you like to encrypt or decrypt a message?\n")
print(encryption)

message = input("Please enter a message to encrypt:\n")
print(message)

multiply_key = input("Please enter a multiplicative key value (1-26)\n")
print(multiply_key)

additive_key = input("Please enter a additive key value (1-26)\n")
print(additive_key)

# Original Alphabet & letter positions
original_alphabet = {"a":0,
                     "b":1,
                     "c":2,
                     "d":3,
                     "e":4,
                     "f":5,
                     "g":6,
                     "h":7,
                     "i":8,
                     "j":9,
                     "k":10,
                     "l":11,
                     "m":12,
                     "n":13,
                     "o":14,
                     "p":15,
                     "q":16,
                     "r":17,
                     "s":18,
                     "t":19,
                     "u":20,
                     "v":21,
                     "w":22,
                     "x":23,
                     "y":24,
                     "z":25}

# Equation

# Cypher Alphabet & letter positions