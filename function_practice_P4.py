from audioop import mul


def max_num(int1, int2, int3):
    return max([int1, int2, int3])
#max_num(4, 9, 8)

def mult_list(list):
    result = 1
    for i in list:
        result = result * i
    return result
#mult_list([2, 6, 2])

def rev_string(string):
    return string[::-1]
#rev_string('hello')

def num_within(num, r1, r2):
    if num >= r1 and num <= r2:
        return(True)
    else:
        return(False)
#num_within(5, 3, 8)

triangle = [[1],[1,1]]
def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
        for row in triangle:
            print(*row)
#pascal(8)