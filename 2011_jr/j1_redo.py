#ccc 2011 j1() redo
def Solution():
    ant = int(input("How many antennas?\n"))
    eye = int(input("How many eyes?\n"))
    
    if ant >= 3 and eye <= 4:
        print('TroyMartian')
    if ant <=6 and eye >= 2:
        print('VladSaturnian')
    if ant <= 2 and eye <= 3:
        print('GraemeMercurian')

        
Solution()
