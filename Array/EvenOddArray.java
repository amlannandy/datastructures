package Array;

public class EvenOddArray {

  public static int getCount(int[] arr) {
    int res = 1, curr = 1;
    for (int i = 1; i < arr.length; i++) {
      if ((arr[i] % 2 == 0 && arr[i-1] % 2 != 0) || (arr[i] % 2 != 0 && arr[i-1] % 2 == 0))
        curr++;
      else
        curr = 1;
      res = Math.max(res, curr);
    }
    return res;
  }

  public static void main(String[] args) {
    
    int[] arr = Basic.inputArray();
    System.out.println("Longest Subarray is " + getCount(arr));

  }
  
}
