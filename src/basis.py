from random import  randint
import              sys

def ft_randint():
    #For debug purposes, waitin to merge w/ 3.1.1
    return (randint(0,4));

def ft_generate_board(n, tuple_):
    """Generate game board, obviously"""
    i = 0;
    j = 0;
    arr = [[0] * n for _ in range(n)];

    while (j < n):
        while (i < n):
            #arr[j][i] = ft_3_1_1(tuple_);
            arr[j][i] = ft_randint();
            i += 1;
        j += 1;
        i = 0;

    print(arr);
    return (arr);

def ft_display_board(arr, size):
    """Display our game board"""
    i = 0;
    j = 0;

    while (j < size):
        while (i < size):
            end_ = " ";
            if ((i + 1) == size):
                end_ = "";
            print(str(arr[j][i]), end=end_);
            i += 1;
        print();
        i = 0;
        j += 1;

ft_display_board(ft_generate_board(int(sys.argv[1]), (0,0,0)), int(sys.argv[1]));
#ft_generate_board(5, (0,0,0));
