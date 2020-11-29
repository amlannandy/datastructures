package Array;

public class RemoveDuplicates {

  public static int removeDupes(int[] arr) {
    int[] temp = new int[arr.length];
    temp[0] = arr[0];
    int res = 1;
    for (int i = 1; i < arr.length; i++) {
      if (arr[i] != temp[res-1]) {
        temp[res] = arr[i];
        res++;
      }
    }
    for (int i = 0; i < temp.length; i++) {
      arr[i] = temp[i];
    }
    return res;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    int res = removeDupes(arr);
    System.out.println("Updated Array is: ");
    for (int i = 0; i < res; i++) {
      System.out.print(arr[i] + " ");
    }
  }
  
}
