package Array;

import java.util.Scanner;

public class Deletion {

  public static void deleteFromArray(int[] arr, int pos) {
    for (int i = pos; i < arr.length - 1; i++) {
      arr[i] = arr[i+1];
    }
  }

  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    int[] arr = Basic.inputArray();
    System.out.print("Enter position: ");
    int pos = scanner.nextInt();
    deleteFromArray(arr, pos);
    System.out.println("Updated Array is:");
    for (int i = 0; i < arr.length - 1; i++) {
      System.out.print(arr[i] + " ");
    }
    scanner.close();
  }
  
}
