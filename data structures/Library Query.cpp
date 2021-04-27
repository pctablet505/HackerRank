#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int t;
    cin >> t;
    for (int e = 0; e < t; e++) {
        int n, q, t, x, y, k, i, l;
        cin >> n;
        int no_books[n + 1];
        no_books[0] = 0;
        for (i = 1; i <= n; i++) {
            cin >> no_books[i];
        }
        cin >> q;
        while (q--) {
            cin >> t;
            if (t == 0) {
                cin >> x >> y >> k;
                int temp[1001];
                for (int j = 1; j < 1001; j++) {
                    temp[j] = 0;
                }
                for (int j = x; j <= y; j++) {
                    temp[no_books[j]]++;
                }
                int sum = 0, ans = 0;
                for (int j = 1; j <= 1000; j++) {
                    sum += temp[j];
                    if (sum >= k) {
                        ans = j;
                        break;
                    }
                }
                cout << ans << endl;
                for (int j = 1; j < 1001; j++) {
                    temp[j] = 0;
                }

            } else {
                cin >> x >> k;
                no_books[x] = k;
            }
        }
    }
    return 0;
}
