package Array;

public class FrequenciesInSortedArray {

  public static void countFrequencies(int[] arr) {
    int n = arr.length;
    int i = 1, freq = 1;
    while (i < n) {
      while (i < n && arr[i] == arr[i-1]) {
        i++;
        freq++;
      }
      System.out.println(arr[i-1] + " -> " + freq);
      i++;
      freq = 1;
    }
  }

  public static void main(String[] args) {
    int[] arr = Basic.inputArray();
    countFrequencies(arr);
  }
  
}
