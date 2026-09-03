import java.util.Scanner;
public class function {
    public static void main(String[] args){
       int r=sum();
       System.out.println("Sum of two numbers is : "+r);
    }
    static int sum(){
        Scanner input=new Scanner(System.in);
         int a=input.nextInt();
        int b=input.nextInt();
        int add=a+b;
        return add;
    }
}
