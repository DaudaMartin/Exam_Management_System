#SET CALCULATOR

class calculator:

    print("""
    DIGITAL INTEGRATED SET OPERATIONS CALCULATOR

    This calculator is designed for all sets calculation.

    Copy right TMR 2022

    """)
    noSets = int(input("Input the number of sets to operate"))
    # for n in range()
    sets = []
    for i in range(0,noSets):
        sets.append(set(input("Enter Sets")))
    for s in sets:
        print(sets)
        break
    else:
        print("Set input completed")
        
    # for s in range(0,noSets):
    #     sets[s] = set(input("Enter Sets "+str(s+1)))
    #     print(sets)

    print("""
    Select your Operation

    1. Union                           4.subset
                    
    2. Intercept                       5.Supersets
                    
    3.Disjoint                         6.Symmetry
    """)
    operation = ("Union","Intercept","Disjoint","Subset","Superset","symmetry")
    if operation:
                oper = input("Select your operation")
                # for o in range(0,7):
                #   print(operation[oper])
    if oper == ("1"):
        print(operation[0])
        set5 = sets[i].union(sets[i])
        print(set5)

    if oper == ("2"):
        print(operation[1])
        set6 = sets[i]
        print(set6)
    if oper == ("3"):
        print(operation[2])
        print(sets[i].isdisjoint(sets[i]))
    if oper == ("6"):
        print(operation[5])
        set7 = sets[i].symmetric_difference_update(sets[i])
        print(set7)


