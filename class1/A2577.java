import java.util.Scanner;
class A2577{
    public static void main(String[]z) {
        try(Scanner s=new Scanner(System.in)){
        int a=s.nextInt();
        int b=s.nextInt();
        int c=s.nextInt(),i;
        long l=(long)a*b*c;
        int[] cnt=new int[10];
        while (l>0){
            cnt[(int)(l%10)]++;
            l/=10;
        }
        for (i=0;i<10;i++){
            System.out.println(cnt[i]);
        }
        }
    }
}