package java_codess;
import java.util.*;
class positive_or_negative{
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);
        int n=s.nextInt();
        if(n>=0){
            if(n==0){
                System.out.println("number is zero");

            }else{
                System.out.println("postive number");
            }
            

        }else{
            System.out.println("negative no");
        }
        s.close();
    }
}