import java.util.Scanner;
class A2753 {
    public static void main(String[] a){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        if (n%4==0 && n%100!=0 || n%400==0){
            System.out.print(1);
        }
        else{
            System.out.print(0);
        }
        s.close();
        }
    }
    
