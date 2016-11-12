#ccc 2013 j3 
def Solution():
    def distinct(year):
        y = str(year)
        for digit in y:
            if y.count(digit) > 1:
                return False
        return True
    
    year = int(input()) + 1
    while not distinct(year):
        year += 1

    print(year)

Solution()
