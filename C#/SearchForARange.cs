public class Solution {
    public int[] SearchRange(int[] nums, int target) {
         int[] arr = new int[2];
            if (nums.Length == 1 && nums[0]==target)
            {
                return arr;
            }
            if (nums.Length == 2 && (nums[0] == nums[1]) && (nums[0] == target))
            {
                arr[1] = 1;
                return arr;
            }
            if (nums.Length == 2 && nums[0] == target)
            {
                return arr;
            }
            if (nums.Length == 2 && nums[1] == target)
            {
                arr[0] = 1;
                arr[1] = 1;
                return arr;
            }
            arr[0] = -1;
            arr[1] = -1;
            int low = 0;
            int high = nums.Length - 1;
            int i = FindIndex(nums, low, high, target);
            int p = 0;
            if (i != -1)
            {
                FillInTheArray(nums, arr, i);
            }
            return arr;
              
    }
    
     private void FillInTheArray(int[] nums, int[] arr, int index)
        {
            int target = nums[index];
            if (index >= 0)
            {
                for (int i = index; i >= 0; --i)
                {
                    if (nums[i] == target)
                    {
                        arr[0] = i;
                    }
                    else
                    {
                        break;
                    }
                }
                for (int i = index; i <= nums.Length - 1; ++i)
                {
                    if (nums[i] == target)
                    {
                        arr[1] = i;
                    }
                    else
                    {
                        break;
                    }

                }
            }
        }
        
         private  int FindIndex(int[] nums, int low, int high, int target)
        {
            if (low > high)
            {
                return -1;
            }
            int mid = (low + high) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] < target)
            {
                low = mid + 1;
                return FindIndex(nums, low, high, target);
            }
            if (nums[mid] > target)
            {
                high = mid - 1;
                return FindIndex(nums, low, high, target);
            }
            return -1;
        }
     
}