package Array;

public class LeftRotate1 {

  public static void leftRotateByOne(int[] arr) {
    int temp = arr[0];
    for (int i = 0; i < arr.length-1; i++) {
      arr[i] = arr[i+1];
    }
    arr[arr.length-1] = temp;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    leftRotateByOne(arr);
    System.out.println("Updated Array is:");
    Basic.printArray(arr);
  }
}
