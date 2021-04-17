package Mathematics;

import java.util.Scanner;

public class NumberOfDigits {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter a number: ");
    int num = scanner.nextInt();
    int res = getNumberOfDigits(num);
    System.out.println("Number of digits - " + res);
    scanner.close();
  }

  public static int getNumberOfDigits(int num) {
    return (int) Math.floor(Math.log10(num) + 1);
  }

}