public class fibonaccinumber {
     public static void main() {

        int a = 0;
        int b = 1;

        for (int i=0; i<=10; i+=1){
            System.out.println(a);
            int temp=a;
            a=b;
            b=temp+b;
        }
    
}
    
}
