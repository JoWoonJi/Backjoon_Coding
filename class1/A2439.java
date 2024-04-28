import java.util.Scanner;
class A2439 {
    public static void main(String[]z){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(),i,j;
        for (i=1;i<=n;i++){
            for (j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            for (j=1;j<=i;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}