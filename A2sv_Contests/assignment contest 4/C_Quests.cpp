#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int max_experience(int n, int k, vector<int>& a, vector<int>& b) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            dp[i][j] = dp[i - 1][j]; // Skip quest i

            if (j >= i) { // Can complete quest i at most j times
                int repeated_exp = 0;
                for (int x = 1; x < min(j, i) + 1; ++x) {
                    repeated_exp += b[i - 1] * x;
                }

                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[i - 1] + repeated_exp);
            }
        }
    }

    return dp[n][k];
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;

        vector<int> a(n), b(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
        }

        cout << max_experience(n, k, a, b) << endl;
    }

    return 0;
}
