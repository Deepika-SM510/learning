import java.util.Scanner;

public class enhancedswitch {
    public static void main (String[] args){
    Scanner input =new Scanner(System.in);
        String fruits=input.next();
        switch(fruits){
            case "Mango"->System.out.println("King of fruits!");
            case "Apple"->System.out.println("Healthiest fruit!");
            case "Orange"->System.out.println("Vitamin C powerhouse!");
            case "Banana"->System.out.println("Great for potassium!");
            default->System.out.println("enter proper fruit name!");

        }

    }


}

