package Array;

public class Merge {
  
  public static int[] mergeArrays(int[] a, int[] b) {
    int[] c = new int[a.length + b.length];
    int k = 0;
    for (int i = 0; i < a.length; i++) {
      c[k] = a[i];
      k++;
    }
    for (int i = 0; i < b.length; i++) {
      c[k] = b[i];
      k++;
    }
    return c;
  }

  public static void main(String[] args) {
    int[] a = Basic.inputArray();
    int[] b = Basic.inputArray();
    int[] c = mergeArrays(a, b);
    System.out.println("Merged Array is:");
    Basic.printArray(c);
  }
}
