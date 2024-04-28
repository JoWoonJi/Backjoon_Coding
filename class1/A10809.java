import java.util.Scanner;
class A10809{
    public static void main(String[]z) {
        Scanner sc=new Scanner(System.in);
        String s= sc.next();
        for (char c='a';c<='z';c++){
            System.out.print(s.indexOf(c)+" ");
        }
        sc.close();
    }
}