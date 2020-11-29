package Array;

import java.util.Scanner;

public class Insertion {

  public static void insertInArray(int[] arr, int n, int item, int pos) {
    for (int i = n; i > pos; i--) {
      arr[i] = arr[i-1];
    }
    arr[pos] = item;
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter size of Array: ");
    int size = scanner.nextInt();
    int[] arr = new int[size+1];
    System.out.println("Enter " + size + " elements: ");
    for (int i = 0; i < size; i++) {
      arr[i] = scanner.nextInt();
    }
    System.out.print("Enter item: ");
    int item = scanner.nextInt();
    System.out.print("Enter position: ");
    int pos = scanner.nextInt();
    insertInArray(arr, size, item, pos);
    System.out.println("Updated Array is:");
    Basic.printArray(arr);
    scanner.close();
  }
}
