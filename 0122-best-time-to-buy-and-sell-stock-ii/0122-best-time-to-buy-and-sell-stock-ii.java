class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int buy = prices[0] ;
        int profit = 0;

        for ( int i = 1 ; i < n ; i++){
            if(prices[i] > buy){
                profit += prices[i] - buy;
                buy = prices[i];
            }
            else{
                buy = prices[i];
            }
        }
        return profit;
    }
}