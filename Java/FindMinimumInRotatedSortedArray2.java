import java.util.ArrayList;
public class Solution {
    public int findMin(int[] nums) {
        if (nums == null) {
            return -1;
        }
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        return (Math.min(funcA(nums), funcB(nums)));
    }
    
    private static int funcA(int[] nums) {
        ArrayList<Integer> temp = new ArrayList<Integer>();
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] - nums[i + 1] >= 0) {
                temp.add(nums[i + 1]);
            }
        }
        if(temp.size()>0) {
            return getMin(temp);
        }
        return nums[0];
    }

    private static int getMin(ArrayList<Integer> nums) {
        int length= nums.size();
        int min = Integer.MAX_VALUE;
        for(int i=0; i < length ; ++i) {
            int x = nums.get(i);
            if(x < min) {
                min = x;
            }
        }
        return min;
    }

    private static int funcB(int[] nums) {
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] < nums[i + 1]) {
                return nums[i];
            }
        }
        return nums[0];
    }
}