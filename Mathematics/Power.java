package Mathematics;

import java.util.Scanner;

public class Power {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter x and y:");
    int x = scanner.nextInt();
    int y = scanner.nextInt();
    System.out.println("(Naive) Result is - " + naiveSolution(x, y));
    System.out.println("(Recursive) Result is - " + recursiveSolution(x, y));
    System.out.println("(Iterative) Result is - " + iterativeSolution(x, y));
    scanner.close();
  }

  public static int naiveSolution(int x, int y) {
    int res = 1;
    for (int i = 0; i < y; i++) {
      res *= x;
    }
    return res;
  }

  public static int recursiveSolution(int x, int y) {
    if (y == 0)
      return 1;
    int temp = recursiveSolution(x, y/2);
    temp *= temp;
    if (y % 2 == 0)
      return temp;
    else
      return temp * x;
  }

  public static int iterativeSolution(int x, int y) {
    int res = 1;
    while (y > 0) {
      if (y % 2 != 0)
        res *= x;
      x *= x;
      y /= 2;
    }
    return res;
  }
  
}
