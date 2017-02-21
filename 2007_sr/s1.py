import sys
import os
with open(os.path.join(sys.path[0], 's1.in')) as f:
    year = 1989
    month = 2
    date = 27
    for i in range(int(f.readline())):
        year1, month1, date1 = map(int, f.readline().split())
        if year1 < year:
            print('Yes')
        elif year1 == year:
            if month1 < month:
                print('Yes')
            elif month1 == month:
                if date1 <= date:
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')
        else:
            print('No')
