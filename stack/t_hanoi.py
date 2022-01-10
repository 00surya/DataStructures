
def T_H(no_of_discs,Tower_1,Tower_2,Tower_3):

    if no_of_discs==1:
        print(f"{Tower_1}-->{Tower_3}")
        return
    
    T_H(no_of_discs-1,Tower_1,Tower_3,Tower_2)
    print(f"{Tower_1}-->{Tower_3}")
    T_H(no_of_discs-1,Tower_2,Tower_1,Tower_3)


Tower_1 = "T1"
Tower_2 = "T2"
Tower_3 = "T3"

no_of_discs = 3
T_H(no_of_discs,Tower_1,Tower_2,Tower_3)

