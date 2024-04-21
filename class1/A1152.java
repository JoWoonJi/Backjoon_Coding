import java.util.Scanner;
class A1152{
    public static void main(String[]z){
        Scanner s=new Scanner(System.in);
        int cnt=0;
        while (s.hasNext()){
            s.next();
            cnt++;
        }
        System.out.print(cnt);
        s.close();
    }
    
}
