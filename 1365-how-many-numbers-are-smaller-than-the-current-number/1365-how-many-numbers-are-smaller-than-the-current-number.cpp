class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
     // 1. create all number array
        vector<int> all_num(101, 0);
        vector<int> out(nums.size());
        // 2. Find the occurance of each number in the array
        for ( int i = 0; i < nums.size(); i++){
            all_num[nums[i]]++;
        }
        
        // 3. Creating a prefix array
        for ( int i = 1; i < all_num.size(); i++){
            all_num[i] += all_num[i-1];
        }
        // inspecting the all_nums array
        for (int i : all_num){
            cout << i << " ";
        }
        // 4. returning the output array
        for (int i = 0; i < nums.size() ; i++){
            if (nums[i] == 0){
            out[i] = 0;
            }
            else{
                out[i] = all_num[nums[i]-1];
            }
        }
        return out;
    }    
};