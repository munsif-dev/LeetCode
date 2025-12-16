class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> out(nums.size());
        for (int i = 0; i < nums.size(); i++){
            int count = 0;
            for (int j = 0; j < nums.size(); j++){
                if (i != j and nums[j] < nums[i]){
                    count++;
                }
            }
            out[i] = count;
        }
        return out;
    }
};