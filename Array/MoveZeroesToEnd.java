package Array;

public class MoveZeroesToEnd {

  public static void moveZeroes(int[] arr) {
    int count = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != 0) {
        swap(arr, i, count);
        count++;
      }
    }
  }

  public static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }

  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    moveZeroes(arr);
    System.out.println("Updated Array is:");
    Basic.printArray(arr);
  }
}
