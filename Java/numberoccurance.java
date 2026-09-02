public class numberoccurance {
    public static void main(String[] args){
        int a=56754352;
        int count=0;
        for (int i=0; i<8; i++){
            
            
            int r=a%10;
            if (r==5){
                count+=1;
            
            }
            a=a/10;
        }
        System.out.println("Number of occurances of 5 in the number is : "+count);    
 
    }
    
}
