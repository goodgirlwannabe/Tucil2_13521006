import numpy as np
import random
import matplotlib.pyplot as plt

def createPoint (num, dim):
    #createPoint using randomize
    #num as number of points
    #dim as dimension of points
    #return a list of num points in dim dimensions
    points = np.zeros((num, dim))
    for i in range(num):
        for j in range(dim):
            points[i][j] = random.randint(1, 100)
    return points

def euclideanDistance (point1, point2, count):
    count = count + 1
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])*(point1[i]- point2[i])
    return np.sqrt(distance), count

def closestBF(points, count):
    #brute force
    distance = euclideanDistance(points[0], points[1], count)
    point1 = points[0]
    point2 = points[1]
    for i in range(len(points)):
        for j in range (1+i, len(points)):
            brute = euclideanDistance(points[i], points[j], count)
            count = count + 1
            if (brute < distance):
                distance = brute
                point1 = points[i]
                point2 = points[j]
    return distance, point1, point2, count


def closestDnC (points, count):
    if (len(points) <= 3):
        return closestBF(points, count)

    else :
        #slice matrix into 2 parts
        half = len(points)//2
        disA, pointA1, pointA2, count= closestDnC(points[:int(half)], count)
        disB, pointB1, pointB2, count = closestDnC(points[int(half):], count)
        if disA < disB:
            distance = disA
            point1 = pointA1
            point2 = pointA2
        else:
            distance = disB
            point1 = pointB1
            point2 = pointB2
        #sStrip
        middle = points[int(half)][0]
        sStrip = []
        for i in range(len(points)):
            if (abs(points[i][0] - middle) < distance).any():
                sStrip.append(points[i])
        #compare sStrip

        for i in range(len(sStrip)):
            for j in range(1+i, len(sStrip)):
                if (abs(sStrip[i][1] - sStrip[j][1]) < distance).any():
                    strip = euclideanDistance(sStrip[i], sStrip[j], count)
                    count = count + 1
                    if strip < distance:
                        distance = strip
                        point1 = sStrip[i]
                        point2 = sStrip[j]
    return distance, point1, point2, count

def plot(points, point1, point2):
    # plot the points
    # d is the dimension of the points
    dim = len(points[0])
    if dim == 2:
        x = points[:, 0]
        y = points[:, 1]
        plt.scatter(x, y, color='black', alpha=0.5, s=10, marker='o')
        plt.scatter(point1[0], point1[1], color='red')
        plt.scatter(point2[0], point2[1], color='red')
        plt.show()
    elif dim == 3:
        x = points[:, 0]
        y = points[:, 1]
        z = points[:, 2]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, color='black' , alpha=0.5, s=10 , marker='o')
        ax.scatter(point1[0], point1[1], point1[2], color='red')
        ax.scatter(point2[0], point2[1], point2[2], color='red')
        plt.show()
    else:
        print('Cannot plot the points in dim dimensions')