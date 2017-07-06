public class Solution {
    public int firstMissingPositive(int[] nums) {
        int c = findMax(nums);
        int[] temp = new int[c+1];
        for(int i=0;i<nums.length;++i) {
            if(nums[i]>0) {
                temp[nums[i]] = nums[i];
            }
        }
        for(int i=1;i<temp.length;++i) {
            if (temp[i] == 0) {
                return i;
            }
        }
        return temp.length;
    }
    
    private int findMax(int[] nums) {
        int max = 0;
        for(int i=0;i<nums.length;++i) {
            if(nums[i]>max) {
                max = nums[i];
            }
        }
        return max;
    }
}