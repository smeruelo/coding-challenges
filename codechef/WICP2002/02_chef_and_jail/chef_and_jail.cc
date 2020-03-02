#include <bits/stdc++.h>

using namespace std;

int m, n, x, y;
vector<vector<int>> jail;

bool aux(int i, int j, int p) {
  if (i == y && j == x) return p >= 0;
  int dy[] = {1, 0, 1};
  int dx[] = {0, 1, 1};
  if (p > 0)
    for (int k = 0; k < 3; k++) {
      int ii = i+dy[k];
      int jj = j+dx[k];
      if (ii > y || jj > x) continue;
      if (aux(ii, jj, p - jail[ii][jj])) return true;
    }
  return false;
}

bool escapable() {
  return aux(0, 0, jail[0][0]);
}

int main() {
  int t;
  cin >> t;
  while (t--) {
    cin >> m >> n >> x >> y;
    x--, y--;
    jail = vector<vector<int>>(m, vector<int>(n));
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        cin >> jail[i][j];
    if (escapable()) cout << "Escape\n";
    else cout << "Died\n";
  }
}
