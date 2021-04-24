package Mathematics;

import java.util.Scanner;

public class NumberOfDigits {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter a number: ");
    int num = scanner.nextInt();
    System.out.println("(Recursive) Number of digits - " + recursiveSolution(num));
    System.out.println("(Iterative) Number of digits - " + iterativeSolution(num));
    System.out.println("(Logarithmic) Number of digits - " + logarithmicSolution(num));
    scanner.close();
  }

  public static int iterativeSolution(int num) {
    int count = 0;
    while (num > 0) {
      count++;
      num /= 10;
    }
    return count;
  }

  public static int recursiveSolution(int num) {
    if (num == 0)
      return 0;
    return 1 + recursiveSolution(num/10);
  }

  public static int logarithmicSolution(int num) {
    return (int) Math.floor(Math.log10(num) + 1);
  }

}