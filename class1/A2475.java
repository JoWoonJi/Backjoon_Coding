import java.util.Scanner;
class A2475{
    public static void main(String[] a){
        try(Scanner s=new Scanner(System.in)){
        int n,x=0,i;
        for (i=0;i<5;i++){
            n=s.nextInt();
            x += n*n;
        }
        System.out.print(x%10);
        }
    }
}