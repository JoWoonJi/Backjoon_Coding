import java.util.Scanner;
class A10869{
    public static void  main(String[]z){
        Scanner s=new Scanner(System.in);
        int a=s.nextInt(),b=s.nextInt();
        System.out.println((a+b)+"\n"+(a-b)+"\n"+(a*b)+"\n"+(a/b)+"\n"+(a%b));
        s.close();
    }
}