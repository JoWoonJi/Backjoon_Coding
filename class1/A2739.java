import java.util.Scanner;
class Main{
    public static void main(String[] a){
            Scanner s=new Scanner(System.in);
            int i,n=s.nextInt();
            for (i=1;i<=9;i++){
                System.out.printf("%d * %d = %d\n", n,i,n*i);
            s.close();
            }
        }
}
