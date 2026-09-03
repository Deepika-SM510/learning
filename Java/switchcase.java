import java.util.Scanner;
public class switchcase{
    public static void main (String[] args){
        Scanner input =new Scanner(System.in);
        String fruits=input.next();
        switch(fruits){
    
            case "Mango":
                System.out.println("King of fruits!");
                break;
            case "Apple":
                System.out.println("Healthiest fruit!");
                break;
            case "Orange":
                System.out.println("Vitamin C powerhouse!");
                break;
            case "Banana":
                System.out.println("Great for potassium!");
                break;
            case "Grapes":
                System.out.println("sweetest fruit!");
                break;
            case "Pineapple":
                System.out.println("Not good at summer");
                break;
            default:
                System.out.println("enter proper fruit name!");
        
        }

}  


}