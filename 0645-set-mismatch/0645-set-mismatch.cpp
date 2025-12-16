#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int expected_sum = n * (n+1)/2;
        int array_sum = 0;
        int uniq_sum = 0;
        for (int i = 0; i < n ; i ++){
            array_sum += nums[i];
        }
        set<int> uniq(nums.begin(),nums.end());
        for (int num : uniq){
            uniq_sum += num;
        }

        return {array_sum-uniq_sum, expected_sum-uniq_sum};

    }
};