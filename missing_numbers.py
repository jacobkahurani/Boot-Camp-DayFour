def find_missing(l1,l2): #Define function called find_missing that takes two arguments
    if l1 == [] and l2 == []: #check if arguments entered are empty lists
        return 0 # if condition above is satisfied return zero
    elif l1 == l2:# Check if arguments entered are equal
        return 0 #if contition satisfied return zero
    s1 = set(l1)# initialize set from list passed as argument
    s2 = set(l2)
    for i in (s1^s2):# perform a symmetric difference of both sets and iterate over result
        print i,#output result from loop