#ccc 2013 j2
def Solution():
    def letters(string):
        for letter in string:
            if letter != "I" and letter != '0' and letter != 'S' and letter != "H" and letter != "Z" and letter != "X" and letter != "N":
                return False
                break

        return True
    
    st = input()
    if not letters(st):
        print('NO')

    elif letters(st):
        print('YES')

Solution()
