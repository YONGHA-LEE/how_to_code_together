def deleteOutlier(int_list):
    """Delelte outlier (not 10-20) int
    
    Arguments:
        int_list {[list of int]} -- [input list]
    
    Returns:
        [list of int] -- [outlier deleted list]
    """
    modified_list = list(filter(lambda x: x>=10 and x<=20, int_list))
    return modified_list