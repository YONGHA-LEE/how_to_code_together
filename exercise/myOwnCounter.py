import sys
from readInputTextFile import readInputTextFile
from deleteOutlier import deleteOutlier
from remainOddOrEven import remainOddOrEven
from countNumOfUnique import countNumOfUnique

def myOwnCounter(filename):
    """Our Final Function
    
    Arguments:
        filename {[string]} -- [input file name]
    
    Returns:
        [int] -- [result]
    """
    all_list = readInputTextFile(filename)
    int_list = deleteOutlier(all_list)
    return countNumOfUnique(int_list)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        filename = "input.txt"
    else:
        filename = sys.argv[1]
    print("Answer in {}".format(myOwnCounter(filename)))
