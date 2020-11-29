package Array;

import java.util.Scanner;

public class Basic {

  public static Scanner scanner = new Scanner(System.in);

  public static int[] inputArray() {
    System.out.print("Enter size of Array: ");
    int size = scanner.nextInt();
    int[] arr = new int[size];
    System.out.println("Enter " + size + " elements: ");
    for (int i = 0; i < size; i++) {
      arr[i] = scanner.nextInt();
    }
    return arr;
  }

  public static void printArray(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}
