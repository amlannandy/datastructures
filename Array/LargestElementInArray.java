package Array;

public class LargestElementInArray {

  public static int findMax(int[] arr, int n) {
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++) {
      if (arr[i] > max)
        max = arr[i];
    }
    return max;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println("Largest element in Array is " + findMax(arr, arr.length));
  }
  
}
