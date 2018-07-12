def remainOddOrEven(int_list):
    """Delete odd or even int by length of list

    Arguments:
        int_list {[list of int]} -- [outlier deleted list]

    Returns:
        [list of int] -- [only odd or even ints]
    """
    modified_list = []
    if (len(int_list) % 2 == 0):
        for i in range(len(int_list)):
            if i % 2 == 1:
                modified_list.append(int_list[i])
    else:
        for i in range(len(int_list)):
            if i % 2 == 0:
                modified_list.append(int_list[i])

    return modified_list
