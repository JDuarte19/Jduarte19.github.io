# welcome to awesome duarte python codinggggg!!!!!
# if you are reading this feel free to email me your thoughts on my mess of code!!!
# thanks ~~~~ mydog!!!!

def decify(password):
    #converts to decimals
    size = len(password)
    bits = [0] * size
    for i in range(size):
        char = password[i]
        x = ord(char)
        bits[i] = bin(x)
        #binify(bits[i])

    print(bits)
    
def binify(decimals):
    #1101011
    size = len(decimals)
    exp = 1
    total = 0
    for i in range(size):
        x = decimals[i]
        total += (exp) * int(x)
        exp *= 2
    print(total)


decify("idk")
binify("1101011")