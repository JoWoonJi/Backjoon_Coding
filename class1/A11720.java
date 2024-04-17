import java.util.Scanner;
class A11720{
    public static void main(String[]a){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(),i,p=0;
        String x=s.next();
        for (i=0;i<n;i++){
            p+=x.charAt(i)-'0';
        }
        System.out.print(p);
        s.close();
    }
}