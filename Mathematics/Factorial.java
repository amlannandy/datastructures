package Mathematics;

import java.util.Scanner;

public class Factorial {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter a number: ");
    int num = scanner.nextInt();
    System.out.println("(Iterative) Factorial is " + iterativeSolution(num));
    System.out.println("(Recursive) Factorial is " + recursiveSolution(num));
    scanner.close();
  }

  public static int iterativeSolution(int num) {
    int res = 1;
    while (num > 0) {
      res *= num;
      num--;
    }
    return res;
  }

  public static int recursiveSolution(int num) {
    if (num == 1)
      return 1;
    return num * recursiveSolution(num-1);
  }
  
}
