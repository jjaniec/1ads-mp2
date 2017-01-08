import sys

def     ft_appendable_in_arr(arr, coords, coordstoadd):
    if (arr[coords[0]][coords[1]] == arr[coordstoadd[0]][coordstoadd[1]]):
        return (0);
    return (1);

def     ft_get_adj_cells(n, arr, coords, tuplarr):
    coordstocheck = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    i = 0;
    print(arr);
    while (i != 4):
        print(coordstocheck[i]);
        x = coords[1] + coordstocheck[i][1];
        y = coords[0] + coordstocheck[i][0];
        print("check (" + str(y) + ", " + str(x) + ")")
        if (x >= 0 and x < n and y >= 0 and y < n):
            if (ft_appendable_in_arr(arr, coords, (y, x)) == 0):
                print("0");
                tuplarr.append((y, x));
        i += 1;
    print(tuplarr);

arr = [[5,5,2,5,1],[5,2,9,7,5],[4,9,9,5,3],[4,2,9,5,4],[4,2,5,1,6]];
ft_get_adj_cells(5, arr, (2,2),[(2,2)]);
