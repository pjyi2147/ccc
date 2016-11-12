def s4():
    whole_list = list(map(int, input().split()))
    holdblood = list(whole_list[:8])
    holdpatient = list(whole_list[8:])
    Total = 0
    blood = list(holdblood)
    patient = list(holdpatient)

    def units(b,p):
        u = min(blood[b], patient[p])
        blood[b] -= u
        patient[b] -= u
        return u

    #start with O- (take all O- as possible)
    Total += units(0,0)

    #O+ (take all O+ first, and then take O-)
    Total = Total + units(1,1) + units(0,1)

    #A- (take all A- first, and then take O-)
    Total = Total + units(2,2) + units(0,2)

    #B- (take all B- first, and then take O-)
    Total = Total + units(4,4) + units(4,4)

    #A+ (take all + first)
    Total = Total + units(3,3) + units(1,3)

    #B+
    Total = Total + units(5,5) + units(1,5)

    #A+ (take left -)
    Total = Total + units(2,3) + units(0,3)

    #B+
    Total = Total + units(4,5) + units(0,5)

    #AB-
    Total = Total + units(6,6) + units(4,6) + units(2,6) + units(0,6)

    #AB+
    Total = Total + units(7,7) + units(6,7) + units(5,7) + units(4,7) + units(3,7) + units(2,7) + units(1,7) + units(0,7)

    print("first order", Total)
    
    total2 = 0
    blood = whole_list[:8]
    patient = whole_list[8:]
    
    # try this second ordering
    total2 = 0
    # O- (take all O- you can)
    total2 = total2 + units(0,0)
    # O+ (take all O+ you can, then take from 0-)
    total2 = total2 + units(1,1) + units(0,1)
    # A- (take all A- you can, then take from 0-)
    total2 = total2 + units(2,2) + units(0,2)
    # B- (take all B- you can, then take from 0-)
    total2 = total2 + units(4,4) + units(0,4)

    # A+ (take all A+ you can, then take from A-)
    total2 = total2 + units(3,3) + units(2,3)
    # B+ (take all B+ you can, then take from B-)
    total2 = total2 + units(5,5) + units(4,5)
    # A+ (take all O+ you can, then take from O-)
    total2 = total2 + units(1,3) + units(0,3) 
    # B+ (take all O+ you can, then take from O-)
    total2 = total2 + units(1,5) + units(0,5)

    # AB- (take all AB- you can, then take from B-, A- or O-)
    total2 = total2 + units(6,6) + units(4,6) + units(2,6) + units(0,6)
    # AB+ (take all AB+ you can, then take from AB-, B+, B-, A+, A-, O+ or O-)
    total2 = total2 + units(7,7) + units(6,7) + units(5,7) + units(4,7) + units(3,7) + units(2,7) + units(1,7) + units(0,7)

    print("second order", total2)

    print(max(Total,total2))


    


s4()
