package Array;

public class CheckIfSorted {
  
  public static boolean checkIfSorted(int[] arr) {
    for (int i = 0; i < arr.length-1; i++) {
      if (arr[i] > arr[i+1])
        return false;
    }
    return true;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println(checkIfSorted(arr) ? "Array is sorted" : "Array is not sorted");
  }
}
