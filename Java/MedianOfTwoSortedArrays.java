public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int arrLength1 = nums1.length;
        int arrLength2 = nums2.length;
        if (arrLength1 == 0 && arrLength2 == 0) {
            return 0;
        }
        if (arrLength1 == 0) {
            return findMedian(nums2);
        }
        if (arrLength2 == 0) {
            return findMedian(nums1);
        }
        if(arrLength1==1 && arrLength2==1) {
            double s = nums1[0] + nums2[0];
            s = s / 2;
            return s;
        }
        return sortAndFind(nums1, nums2, arrLength1, arrLength2);
    }
     private double sortAndFind(int[] nums1, int[] nums2, int arrLength1, int arrLength2) {
        int arrlength3 = arrLength1 + arrLength2;
        int stopPoint = (arrlength3 / 2);
        int[] finalArray = new int[arrlength3];
        int k = 0;
        int i = 0;
        int j = 0;
        for (; i <= nums1.length - 1 && j <= nums2.length - 1;) {
            if (nums1[i] < nums2[j]) {
                finalArray[k] = nums1[i];
                ++k;
                ++i;
            }
            else if (nums1[i] > nums2[j]) {
                finalArray[k] = nums2[j];
                ++k;
                ++j;
            }
            else if (nums1[i] == nums2[j]) {
                finalArray[k] = nums1[i];
                ++k;
                ++i;
                finalArray[k] = nums2[j];
                ++j;
                ++k;
            }
            if (k > stopPoint) {
                break;
            }
        }
        if (i < nums1.length - 1 ) {
            while (i < nums1.length && k <= stopPoint) {
                finalArray[k] = nums1[i];
                ++k;
                ++i;
            }
        }
        if (j < nums2.length ) {
            while (j < nums2.length && k <= stopPoint) {
                finalArray[k] = nums2[j];
                ++k;
                ++j;
            }
        }
        if (arrlength3 % 2 == 0) {
            double result = (finalArray[stopPoint - 1] + finalArray[stopPoint]);
            result = result / 2;
            return result;
        }
        else {
            return finalArray[stopPoint];
        }
    }

    private  double findMedian(int[] num) {
        int arrLength = num.length;
        int mod = arrLength % 2;
        int mid = arrLength / 2;
        if (mod == 0) {
            double result = (num[mid - 1] + num[mid]);
            result = result / 2;
            return result;
        }
        if (mod == 1) {
            return num[mid] ;
        }
        return 0;
    }
}