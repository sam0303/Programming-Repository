import java.util.Scanner;
 
public class Main {
 
 public static void main(String[] args) {
  Scanner input = new Scanner(System.in);
  int[] numbers = new int[10];
  int number, i = 0, j, k = 0;
  System.out.print("Enter ten numbers:");
 
  while (k < 10) {
   number = input.nextInt();
   k++;
 
   for (j = 0; j <= i; j++) {
    if (number == numbers[j]) {
     break;
    }
   }
 
   if (j - i == 1) {
    numbers[i] = number;
    i++;
   }
 
  }
 
  System.out.println("The number of distinct number is " + i);
  System.out.print("The distinct numbers are:");
 
  for (int j2 = 0; j2 < i; j2++) {
   System.out.print(numbers[j2] + " ");
  }
 
 }
}
