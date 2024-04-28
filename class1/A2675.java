import java.util.Scanner;
class A2675{
    public static void main(String[]z){
        Scanner x=new Scanner(System.in);
        int t=x.nextInt();
        while (t-->0){
            int r=x.nextInt();
            String s=x.next();
            for (char c:s.toCharArray()){
                for (int i=0;i<r;i++) {
                    System.out.print(c);
                }
            }
            System.out.println();
        }
        x.close();
    }
}