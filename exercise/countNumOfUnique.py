def countNumOfUnique(int_list):
    uniq = []
    for x in int_list :
        if x not in uniq :
            uniq.append(x)
    
    num_of_uniq = len(uniq)
    
    return num_of_uniq