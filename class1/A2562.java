import java.util.Scanner;
class A2562{
    public static void main(String[]a){
        try(Scanner s=new Scanner(System.in)){
        int[] n=new int[9];
        int m=-1,idx=0,i;
        for (i=0;i<9;i++){
            n[i]=s.nextInt();
            if (n[i]>m){
                m=n[i];
                idx=i;
            }
            }
        System.out.println(m);
        System.out.print(idx+1);
        }
        }
}