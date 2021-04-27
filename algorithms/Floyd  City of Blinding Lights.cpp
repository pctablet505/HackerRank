#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int arr[n][n];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            arr[i][j] = 1000000;
    int x, y, r;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> r;
        x--;
        y--;
        if (x == y) {
            arr[x][y] = 0;
        } else arr[x][y] = r;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) arr[i][j] = 0;
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
            }
        }
    }
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<n;j++){
    //         cout << arr[i][j] <<" ";
    //     }
    //     cout << endl;
    // }    
    int z;
    cin >> z;
    int a, b;
    for (int i = 0; i < z; i++) {
        cin >> a >> b;
        if (arr[a - 1][b - 1] == 1000000)
            cout << -1 << endl;
        else cout << arr[a - 1][b - 1] << endl;
    }

    return 0;
}
