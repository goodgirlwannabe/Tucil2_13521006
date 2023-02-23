#include <iostream>
#include "function.hpp"

using namespace std;

int main(){
    int n, d;
    cout << "Enter the number of dimensions: ";
    cin >> d;
    cout << "Enter the number of points: ";
    cin >> n;
    randomize(n, d);
    getDistanceBetweenPoints(points, n);
}