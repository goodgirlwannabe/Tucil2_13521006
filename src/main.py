from function import *

print ("""
    __  _        ___    _____  ___  _____ ______      ____   ____  ____  ____  
   /  | | |     /   \ / ____/ /  _]/ ___/|      |    |    \ /    ||    ||    \ 
  /  /  | |    |     (   \_  /  [_(   \_ |      |    |  o  )  o  | |  | |  D  )
 /  /   | |___ |  O  |\__  ||    _]\__  ||_|  |_|    |   _/|     | |  | |    / 
/   \_  |     ||     |/  \ ||   [_ /  \ |  |  |      |  |  |  _  | |  | |    \ 
\     | |     ||     |\    ||     |\    |  |  |      |  |  |  |  | |  | |  .  \\
 \____| |_____| \___/  \___||_____| \___|  |__|      |__|  |__|__||____||__|\_|
                                                                              
""")

print ("START? (Y/N)")
start = input()
if start == "Y" or start == "y":
    print('Enter the number of dimensions:')
    dim = int(input())
    print('Enter the number of points:')
    num = int(input())
    count = 0
    points = createPoint(num, dim)
    print(points)
    distance, point1, point2, count = closestDnC(points, count)
    print('The closest distance is: ', distance)
    print('The first point is: ', point1)
    print('The second point is: ', point2)
    print('The number of Euclidean calls: ', count)
    plot(points, point1, point2)
elif start == "N" or start == "n":
    print('Goodbye')
else:
    print('Invalid input')
    print('Goodbye')