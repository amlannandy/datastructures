package Mathematics;

import java.util.Scanner;

public class Palindrome {

  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter num: ");
    int num = scanner.nextInt();
    String res = isPalindrome(num) ? "Palindrome" : "Not Palindrome";
    System.out.println(res);
    scanner.close();
  }

  public static boolean isPalindrome(int num) {
    int org = num;
    int rev = 0;
    while (num > 0) {
      int rem = num % 10;
      rev = rev * 10 + rem;
      num /= 10;
    }
    return rev == org;
  }
  
}
