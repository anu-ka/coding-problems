public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums.length == 0) {
            return -1;
        }

        if (nums.length == 1) {
            return 0;
        }

        if (nums.length == 2) {
            if (nums[0] > nums[1]) {
                return 0;
            }
            return 1;
        }

        int index = -1;
        for (int i = 0; i < nums.length - 2; ++i) {
            if (nums[i] - nums[i + 1] < 0 && nums[i + 1] - nums[i + 2] > 0) {
                return i + 1;
            }

            if (nums[i] > nums[i + 1] && index == -1) {
                index = i;
            }
        }

        if (index == -1) {
            if (nums[nums.length - 1] > nums[nums.length - 2]) {
                index = nums.length - 1;
            }
        }        
        return index;
    }
}