import java.util.Scanner;
class A10818{
    public static void main(String[]z){
        try(Scanner s=new Scanner(System.in)){
        int n=s.nextInt(),i,min=Integer.MAX_VALUE,max=Integer.MIN_VALUE;
        int[] l=new int[n];
        for (i=0;i<n;i++){
            l[i]=s.nextInt();
        }
        for (i=0;i<n;i++){
            if (l[i]<min){
                min=l[i];
            }
            if (l[i]>max){
                max=l[i];
            }
        }
        System.out.print(min+" "+max);
    }
    }
}