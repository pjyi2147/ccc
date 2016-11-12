#2012 ccc j4 BigBangSecrets
#this uses ord() and chr() function
#if you don't know them, then google it and find out what it is!
#note that ord('A') = 64 and ord('Z') = 90

def Solution():
    k = int(input()) 
    cyp = input()
    position = 1
    dyp = ''
    for i in range(len(cyp)):
        s = 3*(i+1)+k
        letter = ord(cyp[i]) 
        if letter - s < 65:
            dyp = dyp + str(chr(letter - s + 26))
        else:
            dyp = dyp + str(chr(letter - s))

            
    print(dyp)


Solution()
