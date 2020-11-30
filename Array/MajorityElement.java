package Array;

public class MajorityElement {

  public static int findMajority(int[] arr) {
    int resIndex = 0;
    int count = 1;
    for (int i = 1; i < arr.length; i++) {
      if (arr[resIndex] == arr[i])
        count++;
      else
        count--;
      if (count == 0) {
        resIndex = i;
        count = 1;
      }
    }
    count = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[resIndex] == arr[i])
        count++;
    }
    if (count <= arr.length/2)
      resIndex = -1;
    return resIndex;
  }

  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    System.out.println("Majority Element is at index " + findMajority(arr));
  }
  
}
