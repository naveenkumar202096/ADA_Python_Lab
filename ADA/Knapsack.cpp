#include<iostream>
using namespace std;
// algo for Knapsack.
// maxWeight = weight of sack
int knapsack(int * weights, int * profits, int n, int maxWeight) {
  
  int ** dp = new int * [n + 1];
  for (int i = 0; i < n + 1; i++) {
    dp[i] = new int[maxWeight + 1];
  } 
  for (int i = 0; i < n + 1; i++) {
    for (int j = 0; j < maxWeight + 1; j++) {
      if (i == 0 || j == 0)
        dp[i][j] = 0;
      else if (weights[i - 1] > j) {
        dp[i][j] = dp[i - 1][j];
      } 
       else {
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + profits[i - 1]);
      }
    }
  }
  return dp[n][maxWeight];
}

int main() {
    // Taking number of item in the sack.
  cout<<"Enter the total number of items: ";
  int n; 
  cin >> n;
  cout<<"Enter the weights of items : ";
  int * weights = new int[n];
  int * profits = new int[n];  
//   Taking user input of item weight.
  for (int i = 0; i < n; i++) {   
    cin >> weights[i];
  }
//   taking user input of item profit with respective to weight.
  cout<<"Enter the profits of items : ";
  for (int i = 0; i < n; i++) {   
    cin >> profits[i];
  }
//   Taking maximum weight of sack in which item to be stored.
  cout<<"Enter the Maxweights of sack : ";
  int maxWeight;
  cin >> maxWeight;
  cout << knapsack(weights, profits, n, maxWeight);
}