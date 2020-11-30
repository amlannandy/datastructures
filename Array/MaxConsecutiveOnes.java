package Array;

public class MaxConsecutiveOnes {

  public static int getMaxOnes(int[] arr) {
    int res = 0, count = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] == 1)
        count++;
      else
        count = 0;
      res = Math.max(res, count);
    }
    return res;
  }

  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println("Max Consecutive Ones is " + getMaxOnes(arr));
  }
  
}
