#ccc 2013 j3 copy answer

def Solution():
    def distinct(year):
        s = str(year)
        for digit in s:
            if s.count(digit) > 1:
                return False

        return True

    y = int(input())
    y += 1
    while not distinct(y):
        y += 1

    print(y)
    
             
            
                           



Solution()
