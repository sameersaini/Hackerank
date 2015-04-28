from math import sqrt

for _ in range(int(input())):
    D,P=(int(x) for x in input().split())
    if D < 0:                               #if D < 0 : print 0 coz absolute value can't be negative.
        print("0")
        continue
    if D==0 and P==0:                       #if D==0 and P==0: then only one pair is possible i.e.(0,0) so print 1. 
        print("1")
        continue
    Discriminant=D**2+4*P                   #find Discriminant
    if Discriminant < 0:                    #if Discriminant is less than zero then , roots cant be real numbers
        print("0")                          #so print 0.
    else:
        square=(int(sqrt(Discriminant)))**2 #find weither Discriminant is a perfect square or not.
        if square == Discriminant:          #if Discriminant is a Perfect Square then Roots are Real Integers.
            if D==0 or Discriminant==0:     #if D==0 or Discriminant==0 then there cant only be two pairs.
                print("2")                  #Example:(0,4) fulflls D==0 and (4,-4) fulfills Disc==0
            else:
                print("4")                  #if these two conditions are not fulfilled,there will be 4 pairs.
        else:
            print("0")                      #if Discriminant is not a perfect square then the roots cant be integers.