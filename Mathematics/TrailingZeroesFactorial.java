package Mathematics;

import java.util.Scanner;

public class TrailingZeroesFactorial {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter num: ");
    int num = scanner.nextInt();
    System.out.println("(Naive) Trailing Zeroes - " + naiveSolution(num));
    System.out.println("(Optimized) Trailing Zeroes - " + optimizedSolution(num));
    scanner.close();
  }

  public static int naiveSolution(int num) {
    int fact = 1;
    while (num >= 1) {
      fact *= num;
      num--;
    }
    int res = 0;
    while (fact % 10 == 0) {
      res++;
      fact /= 10;
    }
    return res;
  }

  public static int optimizedSolution(int num) {
    int res = 0;
    for (int i=5; i<num; i*=5) {
      res += num/i;
    }
    return res;
  }
  
}
