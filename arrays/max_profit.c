// max_profit.c
// Problem: Best Time to Buy and Sell Stock (LeetCode 121)
// Approach: Single-pass min tracking — update max profit as prices evolve

int maxProfit(int* prices, int pricesSize) {
    int n=pricesSize,profitnow,min_profit=prices[0],max_profit=0;
    for(int i=0;i<n;i++)
    {
        profitnow=prices[i]-min_profit;
        if(profitnow>max_profit)
            max_profit=profitnow;
        if(prices[i]<min_profit)
            min_profit=prices[i];
    }

    return max_profit;
}
