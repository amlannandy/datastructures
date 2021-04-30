package Mathematics;

import java.util.Scanner;

public class GreatestCommonDivisor {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter num 1: ");
    int a = scanner.nextInt();
    System.out.print("Enter num 2: ");
    int b = scanner.nextInt();
    System.out.println("(Naive) GCD is " + naiveSolution(a, b));
    System.out.println("(Eucldian) GCD is " + euclidianSolution(a, b));
    scanner.close();
  }

  public static int naiveSolution(int a, int b) {
    int res = Math.min(a, b);
    while (res > 0) {
      if (a % res == 0 && b % res == 0)
        break;
      res--;
    }
    return res;
  }

  public static int euclidianSolution(int a, int b) {
    if (b == 0)
      return a;
    return euclidianSolution(b, a%b);
  }
  
}
