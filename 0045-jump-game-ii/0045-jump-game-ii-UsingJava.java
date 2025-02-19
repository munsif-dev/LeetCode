class Solution {
    public int jump(int[] nums) {
    
        int n = nums.length;
        int goal = n-1;
        int i = 0;
        int jumps = 0;
        
        if (n == 1) return 0;
        
        while(goal != 0 ){
            
            if (i + nums[i] >= goal){
                goal = i;
                jumps++;
                i = 0;
                continue;
            }
            i++;

        }
        return jumps;
    }
}