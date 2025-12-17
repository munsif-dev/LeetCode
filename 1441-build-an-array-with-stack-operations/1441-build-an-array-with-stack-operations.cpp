class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> out;
        int m = target.size();
        int j = 0;
        int i = 1;
        while(i <= n && j < m){
            if (target[j] == i){
                j++;
                i++;
                out.push_back("Push");
            }
            else{
                out.push_back("Push");
                out.push_back("Pop");
                i++;
            }
        }
        return out;
    }
};