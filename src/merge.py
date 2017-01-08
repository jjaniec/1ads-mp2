import sys

def     ft_appendable_in_arr(arr, coords, coordstoadd):
    if (arr[coords[0]][coords[1]] == arr[coordstoadd[0]][coordstoadd[1]]):
        return (0);
    return (1);

def     ft_get_adj_cells(n, arr, coords, li):
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
                li.append((y, x));
        i += 1;
    print(li);

def     ft_change_cells_vals(n, arr, li):
    i = 1;
    arr[li[0][0]][li[0][1]] += 1;
    while (i < len(li)):
        arr[li[i][0]][li[i][1]] = 0;
        print(li[i])
        print(arr)
        i += 1;
    print(li);
    print(arr);

tupl = (2,2);
li = [tupl];
arr = [[8,8,2,8,1],[8,2,8,8,8],[4,8,8,8,3],[4,2,8,8,4],[4,2,8,1,6]];
ft_get_adj_cells(5, arr, tupl, li);
ft_change_cells_vals(5, arr, li);

