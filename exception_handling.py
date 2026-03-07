#exception handling in dictionary
d={'a':1,'b':2,'c':3}
try:
    print(d['d'])
except KeyError as e:
    print("Key error! Key 'd' not found in the dictionary.")