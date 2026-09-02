public class reverse {
    public static void main(String[] args){
        int a=6785248;
        int count=0;
        int rev=0;
        for (int i=0; i<7; i++){
            int r=a%10;
            rev=rev*10+r;
            a=a/10;
        }
        System.out.println("Reversed number is : "+rev);    
 
    }
    

}
