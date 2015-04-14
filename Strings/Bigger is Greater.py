T=int(input())
for _ in range(T):
    W=list(input())                         #create a list of string recieved from the user.
    FC_index=len(W)-2
    temp=FC_index   
    
    while temp != -1:                       #find the rightmost character which is smaller than the next character. 
        if W[temp] < W[temp+1]:             #call this character as first character.
            FC_index=temp
            break
        temp -= 1
        
        
    Larger_index={}                         #create a dictionary for holding those characters along with their indexes
                                            #which are to the right of first character.
    for index in range(FC_index+1,len(W)):
        if W[index] > W[FC_index]:
            Larger_index[W[index]]=index
    
    if len(Larger_index) != 0:              #Sort the dictionary according to keys and obtain the first key and its
        Ciel_char=sorted(Larger_index)[0]   #value.CALL THIS CHARACTER AS CIEL CHARACTER
        Ciel_index=Larger_index[Ciel_char]
        
              
        temp_char=W[FC_index]               #swap the first character with then ciel character.
        W[FC_index]=W[Ciel_index]
        W[Ciel_index]=temp_char
        
        New_string=W[:FC_index+1]+sorted(W[FC_index+1:])    #finally sort the substring starting from the next
        print(''.join(New_string))                          #character of the first character to the end of the word. 
    else:
        print("no answer")
    