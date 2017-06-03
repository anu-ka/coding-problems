// Solution to : https://leetcode.com/problems/find-peak-element
public class Solution {
    public int FindPeakElement(int[] nums) {
        if (nums.Length == 0) {
            return -1;
        }

        if (nums.Length == 1) {
            return 0;
        }

        if (nums.Length == 2) {
            if (nums[0] > nums[1]) {
                return 0;
            }
            return 1;
        }

        int index = -1;
        for (int i = 0; i < nums.Length - 2; ++i) {
            if (nums[i] - nums[i + 1] < 0 && nums[i + 1] - nums[i + 2] > 0) {
                return i + 1;
            }

            if (nums[i] > nums[i + 1] && index == -1) {
                index = i;
            }
        }

        if (index == -1) {
            if (nums[nums.Length - 1] > nums[nums.Length - 2]) {
                index = nums.Length - 1;
            }
        }
        
        return index;
    }
}