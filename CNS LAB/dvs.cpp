#include <iostream>
#include <stdio.h>
#define MAXSIZE=50
using namespace std;

struct node
{
    int dist[MAXSIZE];
    int from[MAXSIZE];
} route[10];

int main()
{
    int distanceMatrix[MAXSIZE][MAXSIZE], numnodes, flag=1;
    
    cout << "Enter no of nodes." << endl;
    cin >> numnodes;
    cout << "Enter the distance matrix:" << endl;
    for (int i = 0; i < numnodes; i++)
    {
        for (int j = 0; j < numnodes; j++)
        {
            cin >> distanceMatrix[i][j];
            distanceMatrix[i][i] = 0;
            route[i].dist[j] = distanceMatrix[i][j];
            route[i].from[j] = j;
        }
    }

    
    while (flag)
    {
        flag = 0;
        for (int i = 0; i < numnodes; i++)
        {
            for (int j = 0; j < numnodes; j++)
            {
                for (int k = 0; k < numnodes; k++)
                {
                    if ((route[i].dist[j]) > (route[i].dist[k] + route[k].dist[j]))
                    {
                        route[i].dist[j] = route[i].dist[k] + route[k].dist[j];
                        route[i].from[j] = k;
                        flag = 1;
                    }
                }
            }
        }
    } 

    for (int i = 0; i < no; i++)
    {
        cout << "Router info for router: " << i + 1 << endl;
        cout << "Dest\tNext Hop\tDist" << endl;
        for (int j = 0; j < no; j++)
            printf("%d\t%d\t\t%d\n", j + 1, route[i].from[j] + 1, route[i].dist[j]);
    }
}