#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <cmath>

using namespace std;

vector<vector<int>> points;
void randomize(int n, int d){
    srand(time(0));
    for(int i = 0; i < n; i++){
        vector<int> point;
        for(int j = 0; j < d; j++){
            point.push_back(rand() % 100);
            cout << point[j] << " ";
        }
        points.push_back(point);
        cout << endl;
    }
}

void getDistanceBetweenPoints(vector<vector<int>> points, int n){
    int d1, d2, dis;
    int count = 0;
    if (n = 2){
        dis = sqrt(pow(points[0][0] - points[1][0], 2) + pow(points[0][1] - points[1][1], 2));
        count += 1;
    }
    else {
        vector <vector<int>> s1 (points.begin(), points.begin() + n/2);
        vector <vector<int>> s2 (points.begin() + n/2, points.end());
        getDistanceBetweenPoints(s1, n/2);
        getDistanceBetweenPoints(s2, n/2);
        dis = min(d1, d2);
        count += 1;
    }
    cout << "Closest distance: " << dis << endl;
    cout << "Number of Euclidean calls: " << count << endl;
}