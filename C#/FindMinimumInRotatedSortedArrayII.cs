public class Solution {
    public int FindMin(int[] nums) {        
        if (nums == null) {
            return -1;
        }
        if (nums.Length == 0) {
            return 0;
        }
        if (nums.Length == 1) {
            return nums[0];
        }
        return (Math.Min(FuncA(nums), FuncB(nums)));        
    }
    
    private static int FuncA(int[] nums) {
        List<int> temp = new List<int>();

        for (int i = 0; i < nums.Length - 1; ++i) {
            if (nums[i] - nums[i + 1] >= 0) {
                temp.Add(nums[i + 1]);
            }
        }
        if(temp.Count>0) {
            return temp.Min();
        }
        return nums[0];
    }

    private static int FuncB(int[] nums) {
        for (int i = 0; i < nums.Length - 1; ++i) {
            if (nums[i] < nums[i + 1]) {
                return nums[i];
            }
        }
        return nums[0];
    }
}