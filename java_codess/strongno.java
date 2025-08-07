import java.util.*;
class strongno{
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("enter an integer");
        int n=s.nextInt();
        int k=n;
        int sum=0,r=0;
        while(n!=0){
            int f=1;
            r=n%10;
            for(int i=1;i<=r;i++){
                f=f*i;
            }
            sum+=f;
            n/=10;
        }
        if(k==sum){
            System.out.println("strong no");
        }else{
            System.out.println("not a strong no");
        }
        s.close();
    }
}