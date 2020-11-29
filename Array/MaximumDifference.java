package Array;

public class MaximumDifference {

  public static int maxDiff(int[] arr) {
    int res = arr[1] - arr[0];
    int minValue = arr[0];
    for (int i = 1; i < arr.length; i++) {
      res = Math.max(res, arr[i]-minValue);
      minValue = Math.min(minValue, arr[i]);
    }
    return res;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println("Maximum Difference is " + maxDiff(arr));
  }
  
}
