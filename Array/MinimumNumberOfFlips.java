package Array;

public class MinimumNumberOfFlips {


  public static void findNumberOfFlips(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
      if (arr[i] != arr[i-1]) {
        if (arr[i] != arr[0])
          System.out.print(i + " -> ");
        else
          System.out.println(i-1);
      }
    }
    if (arr[arr.length - 1] != arr[0])
      System.out.println(arr.length - 1);
  }

  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    findNumberOfFlips(arr);
  }
  
}
