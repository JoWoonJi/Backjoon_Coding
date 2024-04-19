import java.util.Scanner;
class A2884{
    public static void main(String[]z){
        Scanner s=new Scanner(System.in);
        int h=s.nextInt(),m=s.nextInt();
        if (m<45){
            h=(h+23)%24;
            m+=15;
        }
        else{
            m-=45;
        }
        System.out.print(h+" "+m);
        s.close();
    }
}
