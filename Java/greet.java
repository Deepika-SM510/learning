public class greet {
    static int a=23;
    public static void main(String[] args){
        a=45;
        System.out.println("Value of a is : "+a);
        int b=20;
        int k=swap(a,b);
        System.out.println(k);
    }
    static int swap(int n, int m){
       int temp=n;
        n=m;
        m=temp;
        return m;
         // or return m, depending on what you want to return
    }
}
