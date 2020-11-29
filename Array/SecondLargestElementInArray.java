package Array;

public class SecondLargestElementInArray {

  public static int findSecondLargest(int[] arr) {
    int largest = Integer.MIN_VALUE;
    int secondLargest = largest;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > largest) {
        secondLargest = largest;
        largest = arr[i];
      }
    }
    return secondLargest;
  }
  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println("Second Largest Element is " + findSecondLargest(arr));                
  }  
}
