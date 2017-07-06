public class Solution {
    public int FirstMissingPositive(int[] nums) {
        int c = FindMax(nums);
        int[] temp = new int[c+1];
        for(int i=0;i<nums.Length;++i) {
            if(nums[i]>0) {
                temp[nums[i]] = nums[i];
            }
        }
        for(int i=1;i<temp.Length;++i) {
            if (temp[i] == 0) {
                return i;
            }
        }
        return temp.Length;
    }
    
    private int FindMax(int[] nums) {
        int max = 0;
        for(int i=0;i<nums.Length;++i) {
            if(nums[i]>max) {
                max = nums[i];
            }
        }
        return max;
    }
}