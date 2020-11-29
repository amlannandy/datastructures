package Array;

import java.util.Scanner;

public class LeftRotateByK {

  public static void leftRotateByK(int[] arr, int k) {
    reverse(arr, 0, k-1);
    reverse(arr, k, arr.length-1);
    reverse(arr, 0, arr.length-1);
  }

  public static void reverse(int[] arr, int start, int end) {
    while (start < end) {
      int temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
  }
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int[] arr = Basic.inputArray();
    System.out.print("Enter k: ");
    int k = scanner.nextInt();
    leftRotateByK(arr, k);
    System.out.println("Updated Array is:");
    Basic.printArray(arr);
    scanner.close();;
  }
  
}
