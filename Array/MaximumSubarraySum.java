package Array;

public class MaximumSubarraySum {

  public static int subarraySum(int[] arr) {
    int res = arr[0], max = arr[0];
    for (int i = 1; i < arr.length; i++) {
      max = Math.max(arr[i], max + arr[i]);
      res = Math.max(res, max);
    }
    return res;
  }

  public static void main(String[] args) {
    
    int[] arr = Basic.inputArray();
    System.out.println("Max Subarray Sum is " + subarraySum(arr));

  }
  
}
