class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> occ_array(n+1,0);
        vector<int> out;
        // create occurance array
        for ( int i = 0; i < n ; i++ ){
            occ_array[nums[i]]++;
        }
        for (int i= 0; i < n+1 ; i++){
            cout << occ_array[i] << " ";
        }
        for (int i = 1; i <= n; i++){
            if (occ_array[i] == 0) out.push_back(i);
        }
        return out;
    }
};