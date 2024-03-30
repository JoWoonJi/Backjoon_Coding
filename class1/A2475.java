import java.util.Scanner;
class A2475{
    public static void main(String[] a){
        try (Scanner s = new Scanner(System.in)) {
            int[] n=new int[5];
            int x=0;
            int i;
            for (i=0;i<5;i++){
                n[i]=s.nextInt();
            }
            for (i=0;i<5;i++){
                x += n[i]*n[i];
            }
            System.out.print(x%10);
        }
    }
}