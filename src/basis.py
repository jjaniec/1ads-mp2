from random import  randint
import              sys

def ft_randint():
    #For debug purposes, waitin to merge w/ 3.1.1
    return (randint(0,4));

def ft_generate_board(n, tuple_):
    """Generate game board, obviously"""
    i = 0;
    j = 0;
    arr = [[0] * n] * n;

    while (j < n):
        while (i < n):
            #arr[j][i] = ft_3_1_1(tuple_);
            arr[j][i] = ft_randint();
            i += 1;
        j += 1
        i = 0;

    #print(arr);
    return (arr)

ft_generate_board(int(sys.argv[1]), (0,0,0));
#ft_generate_board(5, (0,0,0));
