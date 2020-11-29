package Array;

public class Reverse {

  public static int[] reverseArray(int[] arr, int size) {
    int left = 0, right = size - 1;
    while (left < right) {
      int temp = arr[left];
      arr[left] = arr[right];
      arr[right] = temp;
      left++;
      right--;
    }
    return arr;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    int[] res = reverseArray(arr, arr.length);
    System.out.println("Reversed Array is: ");
    Basic.printArray(res);
  }
}
