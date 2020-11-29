package Array;

public class LeadersInArray {

  public static void findLeaders(int[] arr) {
    int max = Integer.MIN_VALUE;
    for (int i = arr.length-1; i >= 0; i--) {
      if (arr[i] > max) {
        System.out.print(arr[i] + " ");
        max = arr[i];
      }
    }
  }
  public static void main(String[] args) {
    
    int[] arr = Basic.inputArray();
    findLeaders(arr);

  }
  
}
