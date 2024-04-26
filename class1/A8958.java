import java.util.Scanner;
class A8958{
    public static void main(String[]z){
        Scanner s=new Scanner(System.in);
        int t=s.nextInt();
        s.nextLine();
        while(t-->0){
            String ox=s.nextLine();
            int score=0,serial=0,i;
            for(i=0;i<ox.length();i++){
                if(ox.charAt(i)=='O'){
                    serial++;
                    score+=serial;
                }else{
                    serial = 0;
                }
            }
            System.out.println(score);
        }
        s.close();
    }
}