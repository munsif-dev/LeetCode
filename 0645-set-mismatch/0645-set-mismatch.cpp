#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> mid_vec(nums.size()+1, 0);
        int dup, missing = -1;
        for (int i = 0; i < nums.size(); i++){
            mid_vec[nums[i]]++;
        }
        for (int i = 1 ; i < mid_vec.size(); i++){
            if (mid_vec[i] == 2) dup = i;
            else if (mid_vec[i] == 0) missing = i;
        }
        return {dup, missing};
    }
};