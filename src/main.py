from function import *

def main():
    print('Enter the number of dimensions:')
    d = int(input())
    print('Enter the number of points:')
    n = int(input())
    points = randomize(n, d)
    # print(len(points))
    # poin = points[0:int(len(points)/2), :]
    # poin2 = points[2:4, :]
    # print(poin)
    # print(poin2)
    getclosest(points, n)
    plot(points)

main()